# DNS-Zone-Disclosure
**DNS Zone Transfer Information Disclosure**

### DNS Zone Disclosure Tool

The `DNS-Zone-Disclosure` tool is designed to identify vulnerabilities related to DNS Zone Transfer Information Disclosure. This tool attempts to perform a DNS zone transfer on a specified domain using a target DNS server. If the zone transfer is successful, it will retrieve and display all the DNS records within the zone file.

#### Features

- **Zone Transfer Attempt:** Tries to perform a DNS zone transfer for the specified domain and DNS server.
- **Record Retrieval:** Retrieves and displays all domain records if the zone transfer is successful.
- **Error Handling:** Includes error handling to report if the zone transfer fails or if any issues occur during the process.

#### Requirements

To run this tool, you need to have Python installed along with the `dnspython` library.

- Python 3.x
- `dnspython` library

#### Installation Guide

1. **Clone the Repository**

   ```bash
   git clone https://github.com/omemishra/DNS-Zone-Disclosure.git
   cd DNS-Zone-Disclosure
   ```

2. **Install Required Dependencies**

   Before running the tool, you need to install the required Python libraries. You can do this using `pip`.

   ```bash
   pip install dnspython
   ```

#### Run Guide

1. **Run the Tool**

   To use the tool, execute the following command in your terminal:

   ```bash
   python DNSzoneDisclosure.py
   ```

2. **Provide Input**

   You will be prompted to enter:

   - **Domain name:** The domain you want to check (e.g., `example.com`)
   - **DNS server IP:** The IP address of the DNS server to perform the zone transfer against.

3. **View Results**

   The tool will attempt the zone transfer and display the DNS records if successful. If the zone transfer fails or no records are retrieved, an appropriate message will be displayed.

#### Usage Example

```bash
python DNSzoneDisclosure.py
Enter the domain name to check: example.com
Enter the DNS server IP: 1.1.1.1
```

*Note: This tool is intended for educational and security assessment purposes to help identify and mitigate DNS Zone Transfer vulnerabilities. Unauthorized use against systems without permission is strictly prohibited.*
