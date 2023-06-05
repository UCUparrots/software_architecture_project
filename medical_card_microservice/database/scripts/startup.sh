#!/bin/bash
PGPASSWORD="postgres" psql -U 'postgres' -d 'medcard_db' -f /opt/app/scripts/create_tables.sql