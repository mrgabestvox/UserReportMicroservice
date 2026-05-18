# UserReportMicroservice

This microservice listens on a port for TCP requests, accepting a single JSON payload from any one connection.

The microservice expects user, service, and report in the format:

payload = {
    "user": "Player One",
    "service": "Interactive Novel",
    "report": "Completed Chapter Two with character Ezekiel."
}

The programs do not retrieve data from the microservice.  The microservice exists for the programs to report user activity
to the developer(s).  It takes whatever reports the programs consider worthy of reporting and prints them to a file corresponding
to the service, for later review by the devs.

I don't believe there's any need for a UML diagram.  All programs submit reports via a single format, and all reports are written to the .txt files
named for whatever service reports them.
