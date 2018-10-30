import os
import argparse
import private_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="Delete the database.", action='store_true')
    args = parser.parse_args()

    if args.d:
        # Should pull password from private_mysql_config.cnf
        # if [Warning] World-writable config file ... is ignored
        # run in bash $ `chmod 400 private_mysql_config.py`
        # private_config.py needs a `DATABASE_NAME = "booking"`
        os.system('mysql --defaults-file=private_mysql_config.cnf -e "DROP DATABASE IF EXISTS {name};"'.format(
            name=private_config.DATABASE_NAME))
        print("Database deleted!")
        os.system(
            'mysql --defaults-file=private_mysql_config.cnf -e "CREATE DATABASE IF NOT EXISTS {name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"'.format(
                name=private_config.DATABASE_NAME))
        print("Database recreated!")
    os.system("export FLASK_APP=booking && export FLASK_DEBUG=true && python3 -m flask run")
