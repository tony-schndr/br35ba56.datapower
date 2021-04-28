/*
     Script Name: getCPU.js
     Purpose: Get Statistics that cannot be produced by the log target on DataPower.
     Revisions:	Version		Date		Author		Description
				1.0.0     	2019		Will Liao	Initial Revision
 */

var sm = require('service-metadata');
var hm = require('header-metadata');
var urlopen = require('urlopen');
var ct = hm.current.get('Content-Type');
var ctx = session.name('getstat') || session.createContext('getstat');
var vAppliance = ctx.getVar('devicename').replace('<?xml version="1.0" encoding="UTF-8"?>','') || 0;
var vDomainName = sm.getVar("var://service/domain-name");
var vLogCategory = {'category':'GetStatCategory'};
var vHost = "https://MGMT:5554/mgmt/status/default/CPUUsage";
var vXMLContentType = "application/json";
	// define the urlopen options
	var options = {
	target : vHost,
	method : 'GET',
	contentType : vXMLContentType,
	timeout : 2
};

// open connection to target and send data over
urlopen.open(options, function (error, response) {
	if (error) {
		// an error occurred during request sending or response header parsing
		console.log('urlopen error: ' + error);
		session.output.write("urlopen connect error: " + error);
	} else {
		// read response data
		// get the response status code
		var responseStatusCode = response.statusCode;
		if (responseStatusCode == 200) {
			response.readAsJSON(function(err, readAsJSONResponse) {
				if (err) {
					session.reject("readAsJSON error: " + JSON.stringify(err));
				} else {
					session.output.write(" Success ");
					
					console.options(vLogCategory).log("Appliance: " + vAppliance + ", CPUUsage: " + JSON.stringify(readAsJSONResponse.CPUUsage.tenSeconds));
				}
			});
			};
		}
	});
