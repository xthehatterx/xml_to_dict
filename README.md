# xml_to_dict

A simple Python XML to Dictionary parser.

The package is based on [this answer](https://stackoverflow.com/a/10077069) from Stack Overflow. It parses entities as well as attributes following [this XML-to-JSON "specification"](https://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html).

I just added the *from_nest* function, which lets you retrieve a value from the nested dictionaries.

## Install

```bash
pip3 install xml_to_dict --user
```

## Usage

```python
from xml_to_dict import XMLtoDict

sample_xml = (
    '<response>'
        '<results>'
            '<user>'
                '<name>Ezequiel</name>'
                '<age>33</age>'
                '<city>San Isidro</city>'
            '</user>'
            '<user>'
                '<name>Belén</name>'
                '<age>30</age>'
                '<city>San Isidro</city>'
            '</user>'
        '</results>'
    '</response>'
)

parser = XMLtoDict(sample_xml)

print(parser.parse()) # {'response': {'results': {'user': [{'name': 'Ezequiel', 'age': '33', 'city': 'San Isidro'}, {'name': 'Belén', 'age': '30', 'city': 'San Isidro'}]}}}

print(parser.from_nest('user')) # [{'name': 'Ezequiel', 'age': '33', 'city': 'San Isidro'}, {'name': 'Belén', 'age': '30', 'city': 'San Isidro'}]
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.