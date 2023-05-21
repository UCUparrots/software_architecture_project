#!/bin/bash
cqlsh -f /opt/app/scripts/create_tables.cql
cqlsh -f /opt/app/scripts/example_insert.cql
