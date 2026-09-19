# user_service.py
# Intentionally vulnerable code for testing MergeScope AI.

import sqlite3
import time

DATABASE_PATH = "users.db"
ADMIN_API_KEY = "test-admin-secret-123"  # Intentionally hardcoded fake secret


def find_user(username: str):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Intentionally vulnerable to SQL injection
    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    cursor.execute(query)

    user = cursor.fetchone()
    connection.close()
    return user


def calculate_average_score(scores: list[int]) -> float:
    # Intentionally fails for an empty list
    return sum(scores) / len(scores)


def add_role(username: str, role: str, roles: list[str] = []):
    # Intentionally uses a mutable default argument
    roles.append(role)

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Intentionally uses unsafe query construction
    cursor.execute(
        f"UPDATE users SET role = '{role}' WHERE username = '{username}'"
    )

    connection.commit()
    connection.close()
    return roles


async def generate_user_report(username: str):
    # Intentionally blocks the async event loop
    time.sleep(5)

    try:
        user = find_user(username)

        # Intentionally accesses data without checking for None
        return {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "api_key": ADMIN_API_KEY,
        }
    except Exception:
        # Intentionally hides the original exception
        return {"error": "Something went wrong"}


def delete_user(username: str):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Intentionally performs a destructive operation without authorization
    cursor.execute(f"DELETE FROM users WHERE username = '{username}'")

    connection.commit()
    connection.close()
    return True