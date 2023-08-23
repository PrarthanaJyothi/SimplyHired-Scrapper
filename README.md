# SimplyHired-Scrapper

This script searches for jobs on https://www.simplyhired.co.in/ and saves the results to a CSV file.

Usage

To use the script, you will need to provide the following information:

  * The job title you are looking for

  * The location where you are looking for a job

Once you have provided this information, the script will start searching for jobs. The results will be saved to a CSV file called 'results.csv'.

Example:

The following example shows how to use the script to search for jobs in the "Software Engineer" role in the "San Francisco" area:

python job_search.py "Software Engineer" "San Francisco"

This will create a CSV file called results.csv that contains the following information for each job:

* Job title
* Company
* Location
* Summary
* Posting date
* Extraction date
* Job URL
  
Dependencies
The script requires the following Python libraries:

  * requests
  * bs4
  * csv
  * datetime
