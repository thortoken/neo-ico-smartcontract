<p align="center">
  <img
    src="https://assets.brandfolder.com/p429iy-cjzaz4-epdy6e/v/1550884/view.png"
    width="125px;">
</p>
<h3 align="center">Thor ICO Smart Contract</h3>
<p align="center">Thor Token Offical ICO Smart Contract.</p>
<p align="center">Author: Leo Rong, Lead Software Developer @ Thor Token</p>
<p align="center"><a href="mailto:leo@thortoken.com" target="_top">leo@thortoken.com</a></p>
<p align="center">Based of Neo ICO Template by Thomas Saunders of the NEX team - https://github.com/neonexchange/neo-ico-template</p>
<hr/>

### Requirements

Usage requires Python 3.6+

### Installation

Clone the repository and navigate into the project directory. 
Make a Python 3 virtual environment and activate it via

```shell
python3 -m venv venv
source venv/bin/activate
```

or to explicitly install Python 3.6 via

```shell
virtualenv -p /usr/local/bin/python3.6 venv
source venv/bin/activate
```

Then install the requirements via

```shell
pip install -r requirements.txt
```

### Compilation

The template may be compiled as follows

```python
python3 compile.py
```


This will compile your template to `ico_smart_contract.avm`

### Import

In neo-python prompt:

```neo-python
import contract ../neo-ico-smartcontract/ico_smart_contract.avm 0702 05 True False
```

### Deploy (Owner Check)

In neo-python prompt:

```neo-python
testinvoke {contract_hash} deploy []
```

### Check circulation and token_sold

In neo-python prompt:

```neo-python
testinvoke {contract_hash} circulation []
testinvoke {contract_hash} token_sold []
```

### Register KYC (Owner Check)

In neo-python prompt:

```neo-python
testinvoke {contract_hash} crowdsale_register ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
testinvoke {contract_hash} crowdsale_status ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
```

### Mint Token (KYC Check)

In neo-python prompt:

```neo-python
testinvoke {contract_hash} mintTokens [] --attach-neo=1
```

### Airdrop - For privatesale (Owner Check and KYC Check)

In neo-python prompt:

```neo-python
testinvoke {contract_hash} airdrop ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y', 1000]
```

### Current Status: Live on MainNet (Tokesale starts at Block 2011901)
#### Token Hash: 67a5086bac196b67d5fd20745b0dc9db4d2930ed

https://neotracker.io/contract/67a5086bac196b67d5fd20745b0dc9db4d2930ed

Thor Token team has deployed the Tokensale Smart Contract onto NEO MainNet!!

