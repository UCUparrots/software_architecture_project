#!/bin/bash

# cqlsh -f /opt/app/scripts/create_tables.cql
# cqlsh -f /opt/app/scripts/example_insert.cql

echo "########################Starting to execute SH script...########################"
# USER_NAME='cassandra'
# PASSWORD='cassandra'

# while ! cqlsh cassandra-node -u "${USER_NAME}" -p "${PASSWORD}" -e 'describe cluster' ; do
while ! cqlsh cassandra-node -e 'describe cluster' ; do
     echo "########################Waiting for main instance to be ready...########################"
     sleep 1
done

for cql_file in ./tmp/cql/*.cql;
do
  # cqlsh cassandra-node -u "${USER_NAME}" -p "${PASSWORD}" -f "${cql_file}" ;
  cqlsh cassandra-node -f "${cql_file}" ;
  echo "########################Script ""${cql_file}"" executed!!!########################"
done
echo "########################Execution of SH script is finished!########################"
echo "########################Stopping temporary instance!########################"