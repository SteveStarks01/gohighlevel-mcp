"""User tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.user import UserCreate, UserUpdate, UserPermissions
from ..params.users import (
    GetUsersParams,
    GetUserParams,
    CreateUserParams,
    UpdateUserParams,
    DeleteUserParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_user_tools(mcp_instance, get_client_func):
    """Register all user tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def get_users(params: GetUsersParams) -> Dict[str, Any]:
        """Get all users"""
        client = await get_client(params.access_token)

        user_list = await client.get_users(
            params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "users": [user.model_dump() for user in user_list.users],
            "count": user_list.count,
            "total": user_list.total,
        }

    @mcp.tool()
    async def get_user(params: GetUserParams) -> Dict[str, Any]:
        """Get a single user by ID"""
        client = await get_client(params.access_token)

        user = await client.get_user(params.user_id)
        return {"success": True, "user": user.model_dump()}

    @mcp.tool()
    async def create_user(params: CreateUserParams) -> Dict[str, Any]:
        """Create a new user in GoHighLevel"""
        client = await get_client(params.access_token)

        # Build permissions if any permission fields are provided
        permissions = None
        if any([
            params.campaigns_enabled, params.campaigns_read_only, params.contacts_enabled,
            params.workflows_enabled, params.workflows_read_only, params.opportunities_enabled,
            params.appointments_enabled, params.conversations_enabled, params.settings_enabled
        ]):
            permissions = UserPermissions(
                campaignsEnabled=params.campaigns_enabled,
                campaignsReadOnly=params.campaigns_read_only,
                contactsEnabled=params.contacts_enabled,
                workflowsEnabled=params.workflows_enabled,
                workflowsReadOnly=params.workflows_read_only,
                opportunitiesEnabled=params.opportunities_enabled,
                appointmentsEnabled=params.appointments_enabled,
                conversationsEnabled=params.conversations_enabled,
                settingsEnabled=params.settings_enabled,
            )

        user_data = UserCreate(
            companyId=params.company_id,
            name=params.name,
            firstName=params.first_name,
            lastName=params.last_name,
            email=params.email,
            phone=params.phone,
            extension=params.extension,
            permissions=permissions,
            roles=params.roles,
            locationIds=params.location_ids,
            profilePhoto=params.profile_photo,
            type=params.user_type,
        )

        user = await client.create_user(user_data)
        return {"success": True, "user": user.model_dump()}

    @mcp.tool()
    async def update_user(params: UpdateUserParams) -> Dict[str, Any]:
        """Update an existing user in GoHighLevel"""
        client = await get_client(params.access_token)

        # Build permissions if any permission fields are provided
        permissions = None
        if any([
            params.campaigns_enabled, params.campaigns_read_only, params.contacts_enabled,
            params.workflows_enabled, params.workflows_read_only, params.opportunities_enabled,
            params.appointments_enabled, params.conversations_enabled, params.settings_enabled
        ]):
            permissions = UserPermissions(
                campaignsEnabled=params.campaigns_enabled,
                campaignsReadOnly=params.campaigns_read_only,
                contactsEnabled=params.contacts_enabled,
                workflowsEnabled=params.workflows_enabled,
                workflowsReadOnly=params.workflows_read_only,
                opportunitiesEnabled=params.opportunities_enabled,
                appointmentsEnabled=params.appointments_enabled,
                conversationsEnabled=params.conversations_enabled,
                settingsEnabled=params.settings_enabled,
            )

        update_data = UserUpdate(
            name=params.name,
            firstName=params.first_name,
            lastName=params.last_name,
            email=params.email,
            phone=params.phone,
            extension=params.extension,
            permissions=permissions,
            roles=params.roles,
            locationIds=params.location_ids,
            profilePhoto=params.profile_photo,
            type=params.user_type,
        )

        user = await client.update_user(params.user_id, update_data)
        return {"success": True, "user": user.model_dump()}

    @mcp.tool()
    async def delete_user(params: DeleteUserParams) -> Dict[str, Any]:
        """Delete a user from GoHighLevel"""
        client = await get_client(params.access_token)

        success = await client.delete_user(params.user_id)
        return {
            "success": success,
            "message": (
                "User deleted successfully"
                if success
                else "Failed to delete user"
            ),
        }
