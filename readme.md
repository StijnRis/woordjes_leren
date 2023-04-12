# Back end

Python version 3.11.2

## Install

pip install -r back_end/requirements.txt

## Start

Set-ExecutionPolicy Unrestricted -Scope Process
.\/back_end/venv/Scripts/Activate.ps1
python back_end/manage.py runserver

## Open Shell:

python manage.py shell

# Front end

## Install

npm install or npm i

## Start

cd front_end
npm run dev

npm run dev --prefix front_end

### Share

npm run dev --prefix front_end --host
