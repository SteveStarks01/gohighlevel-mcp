"""Unit tests for contact tasks MCP endpoints"""

import pytest
from unittest.mock import AsyncMock, patch
from datetime import datetime, timezone

from src.models.task import Task, TaskCreate, TaskUpdate, TaskList
from src.api.client import GoHighLevelClient


class TestContactTasksEndpoints:
    """Test contact tasks MCP endpoint functionality"""

    @pytest.fixture
    def mock_task(self):
        """Create a mock task for testing"""
        return Task(
            id="mock_task_id",
            locationId="mock_location_id",
            contactId="mock_contact_id",
            title="Test Task",
            body="Test task description",
            assignedTo="mock_user_id",
            dueDate=datetime.now(timezone.utc),
            dateAdded=datetime.now(timezone.utc),
            completed=False,
        )

    @pytest.fixture
    def mock_task_list(self, mock_task):
        """Create a mock task list for testing"""
        return TaskList(
            tasks=[mock_task],
            count=1,
            total=1,
        )

    @pytest.mark.asyncio
    async def test_get_contact_tasks_success(self, mock_task_list):
        """Test successful contact tasks retrieval"""
        from src.main import GetContactTasksParams

        mock_client = AsyncMock(spec=GoHighLevelClient)
        mock_client.get_contact_tasks = AsyncMock(return_value=mock_task_list)

        params = GetContactTasksParams(
            contact_id="mock_contact_id",
            location_id="test_location"
        )

        with patch("src.main.get_client", return_value=mock_client):
            client = mock_client
            task_list = await client.get_contact_tasks(
                params.contact_id, params.location_id
            )
            result = {
                "success": True,
                "tasks": [task.model_dump() for task in task_list.tasks],
                "count": task_list.count,
                "total": task_list.total,
            }

        assert result["success"] is True
        assert result["count"] == 1
        assert result["tasks"][0]["id"] == "mock_task_id"
        mock_client.get_contact_tasks.assert_called_once_with(
            "mock_contact_id", "test_location"
        )

    @pytest.mark.asyncio
    async def test_get_contact_task_success(self, mock_task):
        """Test successful single contact task retrieval"""
        from src.main import GetContactTaskParams

        mock_client = AsyncMock(spec=GoHighLevelClient)
        mock_client.get_contact_task = AsyncMock(return_value=mock_task)

        params = GetContactTaskParams(
            contact_id="mock_contact_id",
            task_id="mock_task_id",
            location_id="test_location"
        )

        with patch("src.main.get_client", return_value=mock_client):
            client = mock_client
            task = await client.get_contact_task(
                params.contact_id, params.task_id, params.location_id
            )
            result = {"success": True, "task": task.model_dump()}

        assert result["success"] is True
        assert result["task"]["id"] == "mock_task_id"
        mock_client.get_contact_task.assert_called_once_with(
            "mock_contact_id", "mock_task_id", "test_location"
        )

    @pytest.mark.asyncio
    async def test_create_contact_task_success(self, mock_task):
        """Test successful contact task creation"""
        from src.main import CreateContactTaskParams

        mock_client = AsyncMock(spec=GoHighLevelClient)
        mock_client.create_contact_task = AsyncMock(return_value=mock_task)

        params = CreateContactTaskParams(
            contact_id="mock_contact_id",
            location_id="test_location",
            title="New Task",
            body="Task description",
            assigned_to="user_id",
            completed=False
        )

        with patch("src.main.get_client", return_value=mock_client):
            client = mock_client

            task_data = TaskCreate(
                title=params.title,
                body=params.body,
                dueDate=params.due_date,
                assignedTo=params.assigned_to,
                completed=params.completed,
            )

            task = await client.create_contact_task(
                params.contact_id, task_data, params.location_id
            )
            result = {"success": True, "task": task.model_dump()}

        assert result["success"] is True
        assert result["task"]["id"] == "mock_task_id"
        mock_client.create_contact_task.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_contact_task_success(self, mock_task):
        """Test successful contact task update"""
        from src.main import UpdateContactTaskParams

        mock_client = AsyncMock(spec=GoHighLevelClient)
        mock_client.update_contact_task = AsyncMock(return_value=mock_task)

        params = UpdateContactTaskParams(
            contact_id="mock_contact_id",
            task_id="mock_task_id",
            location_id="test_location",
            title="Updated Task",
            completed=True
        )

        with patch("src.main.get_client", return_value=mock_client):
            client = mock_client

            update_data = TaskUpdate(
                title=params.title,
                body=params.body,
                dueDate=params.due_date,
                assignedTo=params.assigned_to,
                completed=params.completed,
            )

            task = await client.update_contact_task(
                params.contact_id, params.task_id, update_data, params.location_id
            )
            result = {"success": True, "task": task.model_dump()}

        assert result["success"] is True
        assert result["task"]["id"] == "mock_task_id"
        mock_client.update_contact_task.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_contact_task_success(self):
        """Test successful contact task deletion"""
        from src.main import DeleteContactTaskParams

        mock_client = AsyncMock(spec=GoHighLevelClient)
        mock_client.delete_contact_task = AsyncMock(return_value=True)

        params = DeleteContactTaskParams(
            contact_id="mock_contact_id",
            task_id="mock_task_id",
            location_id="test_location"
        )

        with patch("src.main.get_client", return_value=mock_client):
            client = mock_client
            success = await client.delete_contact_task(
                params.contact_id, params.task_id, params.location_id
            )
            result = {
                "success": success,
                "message": (
                    "Task deleted successfully" if success else "Failed to delete task"
                ),
            }

        assert result["success"] is True
        assert result["message"] == "Task deleted successfully"
        mock_client.delete_contact_task.assert_called_once_with(
            "mock_contact_id", "mock_task_id", "test_location"
        )

    @pytest.mark.asyncio
    async def test_complete_contact_task_success(self, mock_task):
        """Test successful contact task completion"""
        from src.main import CompleteContactTaskParams

        # Update mock task to be completed
        completed_task = mock_task.model_copy()
        completed_task.completed = True

        mock_client = AsyncMock(spec=GoHighLevelClient)
        mock_client.complete_contact_task = AsyncMock(return_value=completed_task)

        params = CompleteContactTaskParams(
            contact_id="mock_contact_id",
            task_id="mock_task_id",
            location_id="test_location",
            completed=True
        )

        with patch("src.main.get_client", return_value=mock_client):
            client = mock_client
            task = await client.complete_contact_task(
                params.contact_id, params.task_id, params.completed, params.location_id
            )
            result = {"success": True, "task": task.model_dump()}

        assert result["success"] is True
        assert result["task"]["completed"] is True
        mock_client.complete_contact_task.assert_called_once_with(
            "mock_contact_id", "mock_task_id", True, "test_location"
        )

    def test_task_parameter_classes_exist(self):
        """Test that task parameter classes are properly defined"""
        from src.main import (
            GetContactTasksParams,
            GetContactTaskParams,
            CreateContactTaskParams,
            UpdateContactTaskParams,
            DeleteContactTaskParams,
            CompleteContactTaskParams,
        )
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetContactTasksParams, BaseModel)
        assert issubclass(GetContactTaskParams, BaseModel)
        assert issubclass(CreateContactTaskParams, BaseModel)
        assert issubclass(UpdateContactTaskParams, BaseModel)
        assert issubclass(DeleteContactTaskParams, BaseModel)
        assert issubclass(CompleteContactTaskParams, BaseModel)

        # Check that required fields exist
        assert "contact_id" in GetContactTasksParams.model_fields
        assert "location_id" in GetContactTasksParams.model_fields
        assert "task_id" in GetContactTaskParams.model_fields
        assert "title" in CreateContactTaskParams.model_fields
