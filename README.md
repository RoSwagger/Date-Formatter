[![Alt Text](https://raw.githubusercontent.com/RoSwagger/RoSwagger-Module/0e9b13b0d133f68850be905d9079bf2ccb968dd1/CreatorProgram.png)](https://discord.roswagger.com)

# RoSwagger Date Formatter

## Overview

The **RoSwagger Date Formatter** is a Python module (`roswagger==2.0`) that allows you to convert date strings into various Discord-compatible timestamp formats. This module utilizes the `dateutil` library to parse ISO 8601 date strings and generate formatted timestamps suitable for Discord.

## Features

- Converts ISO 8601 date strings into multiple Discord timestamp formats.
- Outputs results in a structured JSON format for easy parsing.
- Supports a variety of format styles.

## Installation

You can install this module via `pip`. Clone the repository or download the module files to your local machine.

```bash
pip install roswagger==2.0

## Formats & How to Use

```python
Format Type |	Description | Example Output
t |	Short Time |	9:06 PM
T |	Long Time |	9:06:40 PM
d |	Short Date |	02/27/2006
D |	Long Date |	February 27, 2006
f |	Short DateTime |	February 27, 2006 9:06 PM
F |	Long DateTime |	Monday, February 27, 2006 9:06 PM
R |	Relative Time |	16 years ago
```

## Request Example

```json
{
    "original_date": "2006-02-27T21:06:40.3Z",
    "iso_format": "2006-02-27T21:06:40.300000+00:00",
    "formatted_timestamp": "<t:1141072000:f>",
    "description": "Short DateTime (ex., February 27, 2006 9:06 PM)",
    "example": "2006-02-27 21:06:40"
}
```

