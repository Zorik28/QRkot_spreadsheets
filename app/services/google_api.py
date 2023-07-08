from aiogoogle import Aiogoogle

from app.core.config import now_datetime, settings


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = {
        'properties': {
            'title': f'Report dated {now_datetime}',
            'locale': 'ru_RU'
        },
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Sheet1',
                'gridProperties': {'rowCount': 300, 'columnCount': 10}
            }
        }]

    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
    spreadsheetid: str,
    wrapper_services: Aiogoogle
) -> None:
    """Gives your personal account access to the documents
    you create on the service account disk.
    """
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_update_value(
    spreadsheetid: str,
    closed_projects: list,
    wrapper_services: Aiogoogle
) -> None:
    """Updates data in a report table."""
    service = await wrapper_services.discover('sheets', 'v4')
    table_body = [
        [f'Report dated {now_datetime}'],
        ['Top projects by closing speed'],
        ['Project name', 'Fundraising duration', 'Description']
    ]
    for project in closed_projects:
        table_body.append(list(map(str, project)))
    updated_body = {
        'majorDimension': 'ROWS',
        'values': table_body
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:E300',
            valueInputOption='USER_ENTERED',
            json=updated_body
        )
    )
