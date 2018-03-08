NAME  
**logview** - refer current and archived log files using shortcuts

SYNOPSIS  
```bash
logview [-f] [-i index] [-o offset] shortcut  
logview -a [-o 0] shortcut
```

DESCRIPTION  
**logview** allows to refer log files by using a shortcut removing the need to type or even know the file location, even for archived files.

OPTIONS  
**-h, \-\-help**
Print a short help page describing the options available in **logview** and exit.

**-a, \-\-all** 
Print all log files in the directory identified by the shortcut. This might help identifying available indexes in log groups or rotated log file versions. If used in combination with the offset option -o, --offset the archive directory is listed instead.

**-f, \-\-follow** 
Open and follow the log file to watch incoming messages.

**-i, \-\-index _index_** 
Substitute {index} placeholder in log file spec to retrieve log files rotated by number or to pickup a file in a numbered log group.

**-l, \-\-list**
Print a list of available shortcuts. This is mainly used to setup bash completition.

**-o, \-\-offset days**
Retrieve archived log file for `day` days in the past.

CONFIGURATION FILES 
**logview** reads everything about the log files it should open from the following locations:

- /etc/logview.yml
- /etc/logview.d/*.yml
- $LOGVIEW_CONF_D/*.yml
- ~/.logview.yml

A simple configuration file looks like this:

```yaml
---

messages:  
  log: /var/log/messages  
  archive: /var/log/messages-%Y%m%d  
  archive_offset: 1

cio:  
  log: /var/log/cloud-init-output.log

system:
  log: /var/log/system.log
  archive: /var/log/system.log.{index}.gz
```

In this example `messages` defines the shortcut to be used when accessing the log file given by the `log` key. If the offset option `-o, --offset` is used the `archive` key is picked up instead. strftime-like specifiers like `%Y`, `%m` and `%d` are replaced by the current date unless shifted using the offset in `archive_offset`. This is especially useful if the date part of the log file name does not match the date of the content in the log file itself.

NOTES
If **logview** was installed using pip/setuptools as privileged user, you may find it useful to setup bash completion by sourcing `/etc/bash_completion.d/logview` in your `.bashrc` file.

EXAMPLES  
To view the messages log, invoke **logview** as:  
```bash
logview messages
```

If **logview** should wait for incoming messages, use:  
```bash
logview -f messages
```

Yesterdays log can be opened using:  
```bash
logview -o 1 messages
```

List all log files available in the directory containing the message log:  
```bash
logview -a messages
```

BUGS  
No known bugs.

AUTHOR
Thorsten Huhn

