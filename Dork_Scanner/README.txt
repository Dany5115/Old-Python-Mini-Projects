A python3 file to check all of the dorks in the "Dorks.xlsx" Excel file.(so yea you'll need the excel file in every versions of the file)
You can add more dorks to the Excel files if you want, currently I used every dorks from:
"https://www.exploit-db.com/google-hacking-database" (last dork: 3/31/2020) so update the dorks after this time.

Flaw: Google stops you after a few seconds, by giving an error: "HTTP Error 429: Too Many Requests"

UPDATE1: found out that you need to sign & set up a google JSON API billing for being provided to do more than 100 search queries per day. more information at: "https://developers.google.com/custom-search/v1/overview"

And also a better programming structure than the first version(v01). but anyway the flaw still exists.
