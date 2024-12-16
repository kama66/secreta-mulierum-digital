<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns="http://www.w3.org/1999/xhtml" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="2.0" exclude-result-prefixes="#all">
    <xsl:output encoding="UTF-8" media-type="text/html" method="xhtml" version="5.0" indent="yes" omit-xml-declaration="yes"/>
    <xsl:import href="./partials.xsl"/>

<!-- create html -->
    <xsl:template match="/">
        <xsl:result-document encoding="utf-8" method="html">
            <html>
                <head> </head>
                <body class="document">
                    <xsl:apply-templates select=".//tei:body"/>
                </body>
            </html>
        </xsl:result-document>
    </xsl:template>
</xsl:stylesheet>