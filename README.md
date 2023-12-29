# phytobase
Learning to build website for interesting chemicals we eat every day.

Overview of the website:
- Each vegetable has a summary note, table of phytochemicals with key details, image of the vegetable as an icon (if available)
- There are also links to the references table and phytochemicals have their own pages through links
- To automate the entry of information prior to upload, each vegetable has an ID (e.g. veg1, veg2...)
- Each phytochemical also has an ID (e.g. phy1, phy2...) which describes its pharmacological properties
- Each reference has an ID (e.g. ref1, ref2)

-Name of the other key pages or areas:
    1) fytospace/index.html
    2) fytospace/vegetables/veg1.html
    3) fytospace/phytochemicals/phy1.html
    4) fytospace/references/ref1.html
    5) fytospace/images/
    6) fytospace/about.html
    7) fytospace/indexes/references_index.html
    8) fytospace/indexes/vegetables_index.html
    9) fytospace/features/feature_ddmmyy.html

Sqlite works in the backend to store the data. It is used to generate static websites.
The tables in sqlite are currently as follows:
- plants (rowID, english_name, scientific_name, type)
- chemicals (rowID, common_name, scientific_name, type, CAS, 
The rowID will also be the ID used for the image name stored if applicable.
- references (rowID, english_name[plant], scientific_name[chemical], 
