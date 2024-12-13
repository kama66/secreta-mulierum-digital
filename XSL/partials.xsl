<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns="http://www.w3.org/1999/xhtml" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs xsl tei" version="2.0">
    <xsl:template match="tei:ab">
        <div class="transcriptionContent" id="pg_{@n}_{substring-after(@facs, '#')}">
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    <xsl:template match="tei:unclear">
        <span class="pop unclear" data-bs-content="Text partiell unleserlich" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:add">
        <span class="pop add" data-bs-content="Hinzufügung" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:gap">
        <span class="pop gap" data-bs-content="Lücke" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
            <xsl:apply-templates/>
            <xsl:value-of select="string()"/>
        </span>
    </xsl:template>
    <xsl:template match="tei:del">
        <span class="pop del" data-bs-content="Tilgung" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:seg">
        <span class="pop seg" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="top">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:metamark">
        <span class="pop meta" data-bs-content="Umstellungszeichen" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:abbr">
        <xsl:variable name="EX" select="following-sibling::tei:expan"/>
        <xsl:choose>
            <xsl:when test="$EX">
                <span class="pop abbr" data-bs-content="{translate($EX, ' &#x9;&#xa;&#x2E17;', '')}" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
                    <xsl:apply-templates/>
                </span>
            </xsl:when>
            <xsl:otherwise>
                <span class="pop abbr" data-bs-content="Abkürzung" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="right">
                    <xsl:apply-templates/>
                </span>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    <xsl:template name="marginalia" match="tei:note">
        <xsl:variable name="p" select="@place"/>
        <xsl:variable name="s" select="@style"/>
        <span>
            <xsl:attribute name="title" select="string('Marginalie')"/>
            <xsl:attribute name="id" select="preceding::tei:lb[1]/[substring-after(@n, 'N0')]"/>
            <xsl:if test="$p">
                <xsl:attribute name="class" select="@place"/>
            </xsl:if>
            <xsl:apply-templates/>
        </span>
        <xsl:if test="$p = 'left'">
            <span class="pgNumbers">
                <xsl:value-of select="replace(substring-after(preceding::tei:lb[1]/@n, 'N0'), '^0', '')"/>
            </span>
        </xsl:if>
    </xsl:template>
    <xsl:template match="tei:foreign">
        <span class="foreign">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:hi">
        <span class="{substring-after(@rendition, '#')}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:fw">
        <span class="{@type}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    <xsl:template match="tei:head">
        <xsl:variable name="page" select="ancestor::tei:ab/[@n]"/>
        <xsl:variable name="ch" select="@xml:id"/>
        <h3 id="{$page}_{$ch}">
            <xsl:apply-templates/>
        </h3>
    </xsl:template>
    <xsl:template match="tei:persName">
        <a class="text-nowrap pop popInfo" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="left" id="{@ref}" href="/persons/index.html{@ref}" data-bs-content="{@key}" onmouseover="this.title='';"
            onclick="saveLinkDestination(this.id)">
            <xsl:apply-templates/>
        </a>
    </xsl:template>
    <xsl:template match="tei:bibl">
        <a class="text-nowrap pop popInfo" data-bs-container="body" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-placement="left" id="{@source}" href="/works/index.html{@source}" data-bs-content="{@corresp}" onmouseover="this.title='';"
            onclick="saveLinkDestination(this.id)">
            <xsl:apply-templates/>
        </a>
    </xsl:template>
    <!-- omit expan -->
    <xsl:template match="tei:expan"> </xsl:template>
    <!-- lb to br & line numbers -->
    <xsl:template match="tei:lb">
        <br id="{substring-after(@n, 'N0')}"/>
        <xsl:if test="not(following::*[1][self::tei:note]) and not(parent::*[self::tei:note]) and not(preceding::*[1][self::tei:note])">
            <span class="pgNumbers">
                <xsl:value-of select="replace(substring-after(@n, 'N0'), '^0', '')"/>
            </span>
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
