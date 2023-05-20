#!/bin/bash
PGPASSWORD="postgres" psql -U 'postgres' -d 'test_db' -f /opt/app/scripts/create_tables.sql