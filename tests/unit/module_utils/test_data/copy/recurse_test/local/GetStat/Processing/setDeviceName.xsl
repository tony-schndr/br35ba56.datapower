<!--
Script Name: setDeviceName.xsl
Purpose: This is to get the device name and set the name to a context variable to be used to id appliance 
Revisions:Version   Date        Author              Description
			1.0.0     2018.10		WKL	              Initial Revision
-->

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:tns="http://www.example.org/tns"
	xmlns:dp="http://www.datapower.com/extensions"
    extension-element-prefixes="dp" 
	exclude-result-prefixes="dp">

	<xsl:output omit-xml-declaration="yes"/>

	<xsl:template match="/">
		<xsl:variable name="vDeviceName">
			<xsl:value-of select="dp:variable('var://service/system/ident')//*[local-name()='device-name']"/>
		</xsl:variable>
		<dp:set-variable name="'var://context/getstat/devicename'" value="$vDeviceName" />
	</xsl:template>


</xsl:stylesheet>