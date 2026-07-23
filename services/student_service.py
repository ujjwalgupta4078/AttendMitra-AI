from database.schema.queries.supabase_client import supabase


def register_student(data):

    response = (
        supabase
        .table("students")
        .insert(data)
        .execute()
    )

    return response