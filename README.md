<p align="center">
  <img
    src="https://assets.brandfolder.com/p429iy-cjzaz4-epdy6e/v/1550884/view.png"
    width="125px;">
</p>
<h3 align="center">Thor ICO Smart Contract</h3>
<p align="center">Thor Token Offical ICO Smart Contract.</p>
<p align="center">Based of Neo ICO Template by NEX team - https://github.com/neonexchange/neo-ico-template</p>
<hr/>

#### Requirements

Usage requires Python 3.6.

#### Installation

Clone the repository and navigate into the project directory. 
Make a Python 3.6 virtual environment and activate it via

```shell
python3.6 -m venv venv
source venv/bin/activate
```

or to explicitly install Python 3.6 via

    virtualenv -p /usr/local/bin/python3.6 venv
    source venv/bin/activate

Then install the requirements via

```shell
pip install -r requirements.txt
```

#### Compilation

The template may be compiled as follows

```python
from boa.compiler import Compiler

Compiler.load_and_save('ico_smart_contract.py')
```


This will compile your template to `ico_smart_contract.avm`


#### Current Status: In Progress

Thor Token engineering team is actively working on the smart contract for both of the upcoming pre-sale & crowd-sale. More information regarding the KYC and Whitelist process will be annouced soon. Please join our Telegram to get the most up to date information about our progress. https://t.me/joinchat/F-UKj1Md5AilZgV9zU0Dwg