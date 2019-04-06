# phpbb-dl

usage: phpbb-dl [-h] [--username USERNAME] [--password PASSWORD]
                [--output OUTPUT] [--reverse] [--incremental] [--full]
                [--checkpoint CHECKPOINT] [--begin BEGIN] [--end END] [--keep]
                [--simulate] [--tunnel TUNNEL]
                url [url ...]

PhpBB Downloader

positional arguments:
  url                   sequence of urls to access, of format:
                        ['<phpbb_root>/login.php', '<phpbb_root>/index.php',
                        '<phpbb_root>/viewforum.php?f=<forum_id>',
                        '<phpbb_root>/viewtopic.php?t=<topic_id>']

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME, -u USERNAME
                        username to supply to remote server if logging in
  --password PASSWORD, -p PASSWORD
                        password to supply to remote server if logging in
  --output OUTPUT, -o OUTPUT
                        output directory
  --reverse, -r         archive newer topics first
  --incremental, -i     save/load progress in <output>/.timestamp.chk
  --full, -f            restart progress in <output>/.timestamp.chk
  --checkpoint CHECKPOINT, -c CHECKPOINT
                        override progress on start with date/time (e.g.
                        2019-04-06T13:25-0400)
  --begin BEGIN, -b BEGIN
                        begin post date/time range (e.g.
                        2019-04-06T13:25-0400)
  --end END, -e END     end post date/time range (e.g. 2019-04-06T13:25-0400)
  --keep, -k            keep session at <output>/.cookies.txt
  --simulate, -s        simulate execution without writing to disk
  --tunnel TUNNEL, -t TUNNEL
                        Proxy Server (e.g. 127.0.0.1:8118)
