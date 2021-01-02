<!-- 
	Script Name: callGetStat.xsl

	Purpose: Get statistics which are not available from logging to output in syslogs. Stylesheet can be placed in XML Manager 

    

        Version      Date           Author		Description

        1.0          2018.09        Will Liao	Initial Creation.

    

-->

<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:dp="http://www.datapower.com/extensions"
    xmlns:dpconfig="http://www.datapower.com/param/config"
    xmlns:webapi="http://www.ibm.com/apimanagement"
    xmlns:func="http://exslt.org/functions"
    xmlns:wxsl="http://www.w3.org/1999/XSL/TransformAlias"
    xmlns:exsl="http://exslt.org/common"
	xmlns:client="http://datapower.com/sslClientProfile"
    extension-element-prefixes="dp dpconfig exsl">

	<xsl:output omit-xml-declaration="yes"/>

	<xsl:template match="/">
		<dp:url-open
			target="http://127.0.0.1:8888/getstat"
			response="ignore"
			http-method="get"
			>
		</dp:url-open>
	</xsl:template>

</xsl:stylesheet>