<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="#all" version="2.0">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="no"/>

    <!-- get each page as a single xml document -->
    <xsl:template match="tei:body">
        <xsl:for-each select="tei:ab">
            <xsl:result-document method="xml" href="{concat('page_',@n,'.xml')}">
                <TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <text>
                        <body>
                            <xsl:copy-of select="current()"/>
                        </body>
                    </text>
                </TEI>
            </xsl:result-document>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
