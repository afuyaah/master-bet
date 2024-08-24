{ pkgs }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.python310Packages.flask
    pkgs.python310Packages.celery
    pkgs.redis
    pkgs.imagemagick6  # or any other package you might need
  ];

  shellHook = ''
    export FLASK_APP=app.py
    export FLASK_ENV=development
    # Start Flask and Celery workers
    echo "Starting Flask and Celery workers..."
    # Run Flask in the background
    flask run &
    # Run Celery workers in the background
    celery -A app.celery worker --loglevel=info &
    celery -A app.celery beat --loglevel=info &
  '';
}
