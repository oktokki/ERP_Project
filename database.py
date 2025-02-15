from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:oak198844!@localhost/erp_system"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ PostgreSQL 연결 성공!")
except Exception as e:
    print(f"❌ DB 연결 실패: {e}")
