from database.schema.queries.supabase_client import supabase

def register_student(student_data):

    try:

        response = (
            supabase
            .table("students")
            .insert(student_data)
            .execute()
        )

        return True, response

    except Exception as e:

        return False, str(e)