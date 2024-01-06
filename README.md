# Flipkart_WebScrapper
This is a web scraping solution for the Flipkart website's mobile search page. The objective is to create a robust and efficient system that extracts pertinent details about mobile phones and stores them in a CSV file for further analysis.

This Python application utilises web scraping techniques to collect data from Flipkart. Its primary emphasis is on the search query "iPhone" and it collects information from various websites. The retrieved data is subsequently placed in a CSV file. Allow us to conduct a comprehensive analysis of it:

Function Definition: geturl(search, page): Creates a URL by combining the search query and the page number. This program constructs the Flipkart search URL by combining the given search phrase and page number using concatenation.

File Manipulation: Generates a CSV file named "results.csv" to store the obtained data.
Outputs the column headings to the CSV file: Product Number, Product Name, Price, Original Price, Discount, Ratings, and Description.
Conducting an iterative procedure across a series of pages.

The geturl() function is employed to provide a Uniform Resource Locator (URL) for every page within the designated range.
Utilises the urlopen method to send a request to Flipkart and retrieves the HTML content of the webpage.
HTML parsing is the act of examining and extracting data from HTML code.

Utilises BeautifulSoup (soup) for parsing the HTML text. Locates all containers (div elements with the class _13oc-S) that enclose the product information on the webpage.
Data extraction is the act of retrieving precise information or data from a source or dataset.

Inside each enclosure: This function retrieves the product name, price, initial price (if available), discount (if available), ratings, and description by examining specific elements of the HTML structure. Processes and purifies the acquired data. Creates the data for every individual product and saves it in the CSV file.

Terminating the CSV file: Terminates the CSV file once all the extracted data has been written.
<img width="854" alt="1" src="https://github.com/DhruviShah101/Flipkart_WebScrapper/assets/124038034/50401ac8-5e1e-46ee-a07a-cc0b4b1e26c2">

<img width="960" alt="2" src="https://github.com/DhruviShah101/Flipkart_WebScrapper/assets/124038034/cb6ebb24-7055-463c-8387-c00179e7f967">
<img width="639" alt="3" src="https://github.com/DhruviShah101/Flipkart_WebScrapper/assets/124038034/e80d3e1f-83c6-4502-b23c-01c7094160c2">


<img width="477" alt="4" src="https://github.com/DhruviShah101/Flipkart_WebScrapper/assets/124038034/8eb82ec8-0374-4a87-88b8-f242361b492a">

<img width="589" alt="5" src="https://github.com/DhruviShah101/Flipkart_WebScrapper/assets/124038034/a27dd0a8-9e8e-4873-ad87-590eb262c369">

<img width="659" alt="6" src="https://github.com/DhruviShah101/Flipkart_WebScrapper/assets/124038034/697b862d-05dd-43b8-94fd-faee370b1b63">


