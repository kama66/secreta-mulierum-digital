<!-- this transformation erroneously grabs the <body>-tag, which needs to be manually corrected in the output -->
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="#all" version="2.0">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="no"/>

<!-- split transformation into two steps -->
    <xsl:template match="/">
        <xsl:variable name="startTrans">
            <xsl:apply-templates select="/*" mode="startTrans"/>
        </xsl:variable>
        <xsl:apply-templates select="$startTrans/*"/>
    </xsl:template>

    <!-- identity transformation -->
    <xsl:template match="@* | node()" mode="#all">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()" mode="#current"/>
        </xsl:copy>
    </xsl:template>

    <!-- add corresponding chapter number -->
    <xsl:template match="tei:head" mode="startTrans">
<xsl:copy>
<xsl:attribute name="xml:id" select="parent::tei:div/[@xml:id]"></xsl:attribute>
    <xsl:apply-templates mode="startTrans"/></xsl:copy>
    </xsl:template>

    <!-- transform div into milestone -->
    <xsl:template match="tei:div" mode="startTrans">
        <xsl:element name="milestone">
            <xsl:attribute name="n" select="@xml:id"/>
            <xsl:attribute name="unit" select="@type"/>
        </xsl:element>
        <xsl:apply-templates mode="startTrans"/>
    </xsl:template>

    <!-- remove p -->
    <xsl:template match="tei:p" mode="startTrans">
        <xsl:apply-templates mode="startTrans"/>
    </xsl:template>

<!-- wrap page content, second step -->
    <xsl:template match="*[tei:pb]">

        <xsl:variable name="ID" select="@xml:id"/>

        <xsl:for-each-group select="node()" group-starting-with="tei:pb">
            <xsl:variable name="chap" select="./preceding::tei:milestone[1]"/>
            <ab n="{@n}" facs="{@facs}">
<xsl:if test="$chap">
<xsl:attribute name="type" select="$chap/@n"></xsl:attribute>
</xsl:if>
                <xsl:apply-templates select="current-group()[not(self::tei:pb)]"/>
            </ab>
        </xsl:for-each-group>

    </xsl:template>
</xsl:stylesheet>
