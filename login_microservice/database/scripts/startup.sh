#!/bin/bash
PGPASSWORD="postgres" psql -U 'postgres' -d 'test_user_db' -f /opt/app/scripts/create_tables.sql