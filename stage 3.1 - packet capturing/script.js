function resolveDomain() {
    const domain = document.getElementById('domainInput').value.trim();
    const resultElement = document.getElementById('result');
    const apiUrl = `https://cloudflare-dns.com/dns-query?name=${domain}&type=A`;

    fetch(apiUrl, {
        headers: {
            'Accept': 'application/dns-json'
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.Answer) {
                const ip = data.Answer[0].data;
                resultElement.textContent = `IP Address for ${domain}: ${ip}`;
            } else {
                resultElement.textContent = `Domain ${domain} not found in DNS database.`;
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            resultElement.textContent = `Error fetching data: ${error.message}`;
        });
}
