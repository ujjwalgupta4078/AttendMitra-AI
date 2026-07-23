import os
from dotenv import load_dotenv
from supabase import create_client, Client

SUPABASE_URL = "https://aczhpaarhafqsuqfwere.supabase.co"
SUPABASE_KEY = "sb_publishable_v8NX2mmnMSG45CVyWlaqfQ_LZsHqgjF"

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)