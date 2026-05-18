# UserReportMicroservice

This microservice listens on a port for TCP requests, accepting a single JSON payload from any one connection.
It then writes the current time, plus the user, service, and report payload into a .txt file named for the service.
If such a file already exists, it writes to the end of it.  If it doesn't, it creates such a file.

The microservice expects user, service, and report in the format:

payload = {
    "user": "Player One",
    "service": "Interactive Novel",
    "report": "Completed Chapter Two with character Ezekiel."
}

The programs do not retrieve data from the microservice.  The microservice exists for the programs to report user activity
to the developer(s).  It takes whatever reports the programs consider worthy of reporting and prints them to a file corresponding
to the service, for later review by the devs.

<img width="336" height="471" alt="Report Microservice UML" src="https://github.com/user-attachments/assets/47d32673-accc-4c15-8ac0-fa242e8a9f96" />
