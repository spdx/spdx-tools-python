<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:j.0="http://usefulinc.com/ns/doap#"
    xmlns="http://spdx.org/rdf/terms#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
  <Snippet rdf:about="http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-Snippet">
    <snippetFromFile>
      <File rdf:about="http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-DoapSource"/>
    </snippetFromFile>
    <name>from linux kernel</name>
    <copyrightText>Copyright 2008-2010 John Smith</copyrightText>
    <licenseComments>The concluded license was taken from package xyz, from which the snippet was copied into the current file. The concluded license information was found in the COPYING.txt file in package xyz.</licenseComments>
    <rdfs:comment>This snippet was identified as significant and highlighted in this Apache-2.0 file, when a commercial scanner identified it as being derived from file foo.c in package xyz which is licensed under GPL-2.0-or-later.</rdfs:comment>
    <licenseConcluded rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
    <licenseInfoInSnippet rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
  </Snippet>
  <SpdxDocument rdf:about="https://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-DOCUMENT">
    <name>Sample_Document-V2.1</name>
    <creationInfo>
      <CreationInfo>
        <created>2010-02-03T00:00:00Z</created>
        <rdfs:comment>This is an example of an SPDX spreadsheet format</rdfs:comment>
        <creator>Tool: SourceAuditor-V1.2</creator>
        <creator>Organization: Source Auditor Inc.</creator>
        <creator>Person: Gary O'Neall</creator>
      </CreationInfo>
    </creationInfo>
    <specVersion>SPDX-2.1</specVersion>
    <externalDocumentRef>
      <ExternalDocumentRef>
        <externalDocumentId>DocumentRef-spdx-tool-2.1</externalDocumentId>
        <spdxDocument rdf:resource="https://spdx.org/spdxdocs/spdx-tools-v2.1-3F2504E0-4F89-41D3-9A0C-0305E82C3301"/>
        <checksum>
          <Checksum>
            <checksumValue>d6a770ba38583ed4bb4525bd96e50461655d2759</checksumValue>
            <algorithm rdf:resource="http://spdx.org/rdf/terms#checksumAlgorithm_sha1"/>
          </Checksum>
        </checksum>
      </ExternalDocumentRef>
    </externalDocumentRef>
    <referencesFile>
      <File rdf:about="https://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-File1">>
        <licenseConcluded>
          <ExtractedLicensingInfo rdf:nodeID="A1">
            <extractedText>/*
 * (c) Copyright 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009 Hewlett-Packard Development Company, LP
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */</extractedText>
            <licenseId>LicenseRef-1</licenseId>
          </ExtractedLicensingInfo>
        </licenseConcluded>
        <artifactOf>
          <j.0:Project>
            <j.0:homepage>http://www.openjena.org/</j.0:homepage>
            <j.0:name>Jena</j.0:name>
          </j.0:Project>
        </artifactOf>
        <licenseComments>This license is used by Jena</licenseComments>
        <fileName>Jenna-2.6.3/jena-2.6.3-sources.jar</fileName>
        <fileType rdf:resource="http://spdx.org/rdf/terms#fileType_archive"/>
        <copyrightText>(c) Copyright 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009 Hewlett-Packard Development Company, LP</copyrightText>
        <licenseInfoInFile rdf:nodeID="A1"/>
        <rdfs:comment>This file belongs to Jena</rdfs:comment>
        <checksum>
          <Checksum>
            <checksumValue>3ab4e1c67a2d28fced849ee1bb76e7391b93f125</checksumValue>
            <algorithm rdf:resource="http://spdx.org/rdf/terms#checksumAlgorithm_sha1"/>
          </Checksum>
        </checksum>
      </File>
    </referencesFile>
    <reviewed>
      <Review>
        <rdfs:comment>This is just an example.  Some of the non-standard licenses look like they are actually BSD 3 clause licenses</rdfs:comment>
        <reviewDate>2010-02-10T00:00:00Z</reviewDate>
        <reviewer>Person: Joe Reviewer</reviewer>
      </Review>
    </reviewed>
    <dataLicense rdf:resource="http://spdx.org/licenses/CC0-1.0"/>
    <hasExtractedLicensingInfo rdf:nodeID="A1"/>
    <reviewed>
      <Review>
        <rdfs:comment>Another example reviewer.</rdfs:comment>
        <reviewDate>2011-03-13T00:00:00Z</reviewDate>
        <reviewer>Person: Suzanne Reviewer</reviewer>
      </Review>
    </reviewed>
    <annotation>
      <Annotation rdf:about="https://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-45">
        <annotationType rdf:resource="http://spdx.org/rdf/terms#annotationType_review"/>
        <rdfs:comment>This is just an example. Some of the non-standard licenses look like they are actually BSD 3 clause licenses</rdfs:comment>
        <annotationDate>2012-06-13T00:00:00Z</annotationDate>
        <annotator>Person: Jim Reviewer</annotator>
      </Annotation>
    </annotation>
    <relationship>
      <Relationship>
        <relationshipType rdf:resource="http://spdx.org/rdf/terms#relationshipType_describes"/>
        <relatedSpdxElement rdf:resource="http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-Package"/>
      </Relationship>
    </relationship>
    <referencesFile>
      <File rdf:about="https://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-File2">
        <copyrightText>Copyright 2010, 2011 Source Auditor Inc.</copyrightText>
        <licenseInfoInFile rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
        <licenseConcluded rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
        <fileType rdf:resource="http://spdx.org/rdf/terms#fileType_source"/>
        <checksum>
          <Checksum>
            <checksumValue>2fd4e1c67a2d28fced849ee1bb76e7391b93eb12</checksumValue>
            <algorithm rdf:resource="http://spdx.org/rdf/terms#checksumAlgorithm_sha1"/>
          </Checksum>
        </checksum>
        <fileName>src/org/spdx/parser/DOAPProject.java</fileName>
      </File>
    </referencesFile>
    <describesPackage>
      <Package rdf:about="http://www.spdx.org/tools#SPDXRef-Package">
        <licenseInfoFromFiles rdf:resource="http://spdx.org/licenses/Apache-1.0"/>
        <downloadLocation>http://www.spdx.org/tools</downloadLocation>
        <filesAnalyzed>true</filesAnalyzed>
        <supplier>Organization:Linux Foundation</supplier>
        <hasFile rdf:nodeID="A0"/>
        <licenseInfoFromFiles rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
        <packageVerificationCode>
          <PackageVerificationCode>
            <packageVerificationCodeValue>4e3211c67a2d28fced849ee1bb76e7391b93feba</packageVerificationCodeValue>
            <packageVerificationCodeExcludedFile>SpdxTranslatorSpdx.txt</packageVerificationCodeExcludedFile>
            <packageVerificationCodeExcludedFile>SpdxTranslatorSpdx.rdf</packageVerificationCodeExcludedFile>
          </PackageVerificationCode>
        </packageVerificationCode>
        <licenseConcluded>
          <ConjunctiveLicenseSet>
            <member>
              <ExtractedLicensingInfo rdf:nodeID="A3">
                <extractedText>This package includes the GRDDL parser developed by Hewlett Packard under the following license:
© Copyright 2007 Hewlett-Packard Development Company, LP

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: 

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. 
The name of the author may not be used to endorse or promote products derived from this software without specific prior written permission. 
THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </extractedText>
                <licenseId>LicenseRef-2</licenseId>
              </ExtractedLicensingInfo>
            </member>
            <member rdf:nodeID="A1"/>
            <member rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
            <member rdf:resource="http://spdx.org/licenses/MPL-1.1"/>
            <member rdf:resource="http://spdx.org/licenses/Apache-1.0"/>
            <member>
              <ExtractedLicensingInfo rdf:nodeID="A4">
                <extractedText>/*
 * (c) Copyright 2009 University of Bristol
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */  </extractedText>
                <licenseId>LicenseRef-4</licenseId>
              </ExtractedLicensingInfo>
            </member>
            <member>
              <ExtractedLicensingInfo rdf:nodeID="A5">
                <rdfs:seeAlso>http://justasample.url.com</rdfs:seeAlso>
                <rdfs:seeAlso>http://people.apache.org/~andyc/neko/LICENSE</rdfs:seeAlso>
                <licenseName>CyberNeko License</licenseName>
                <rdfs:comment>This is tye CyperNeko License</rdfs:comment>
                <extractedText>The CyberNeko Software License, Version 1.0

 
(C) Copyright 2002-2005, Andy Clark.  All rights reserved.
 
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer. 

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in
   the documentation and/or other materials provided with the
   distribution.

3. The end-user documentation included with the redistribution,
   if any, must include the following acknowledgment:  
     "This product includes software developed by Andy Clark."
   Alternately, this acknowledgment may appear in the software itself,
   if and wherever such third-party acknowledgments normally appear.

4. The names "CyberNeko" and "NekoHTML" must not be used to endorse
   or promote products derived from this software without prior 
   written permission. For written permission, please contact 
   andyc@cyberneko.net.

5. Products derived from this software may not be called "CyberNeko",
   nor may "CyberNeko" appear in their name, without prior written
   permission of the author.

THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR OTHER CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT 
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR 
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</extractedText>
                <licenseId>LicenseRef-3</licenseId>
              </ExtractedLicensingInfo>
            </member>
          </ConjunctiveLicenseSet>
        </licenseConcluded>
        <sourceInfo>Version 1.0 of the SPDX Translator application</sourceInfo>
        <checksum>
          <Checksum>
            <checksumValue>2fd4e1c67a2d28fced849ee1bb76e7391b93eb12</checksumValue>
            <algorithm rdf:resource="http://spdx.org/rdf/terms#checksumAlgorithm_sha1"/>
          </Checksum>
        </checksum>
        <packageFileName>spdxtranslator-1.0.zip</packageFileName>
        <description>This utility translates and SPDX RDF XML document to a spreadsheet, translates a spreadsheet to an SPDX RDF XML document and translates an SPDX RDFa document to an SPDX RDF XML document.</description>
        <licenseInfoFromFiles rdf:nodeID="A4"/>
        <name>SPDX Translator</name>
        <versionInfo>Version 0.9.2</versionInfo>
        <licenseInfoFromFiles rdf:nodeID="A1"/>
        <hasFile rdf:nodeID="A2"/>
        <licenseInfoFromFiles rdf:nodeID="A3"/>
        <copyrightText> Copyright 2010, 2011 Source Auditor Inc.</copyrightText>
        <licenseDeclared>
          <ConjunctiveLicenseSet>
            <member rdf:nodeID="A3"/>
            <member rdf:nodeID="A1"/>
            <member rdf:resource="http://spdx.org/licenses/Apache-2.0"/>
            <member rdf:resource="http://spdx.org/licenses/MPL-1.1"/>
            <member rdf:nodeID="A4"/>
            <member rdf:nodeID="A5"/>
          </ConjunctiveLicenseSet>
        </licenseDeclared>
        <licenseInfoFromFiles rdf:nodeID="A5"/>
        <originator>Organization:SPDX</originator>
        <licenseComments>The declared license information can be found in the NOTICE file at the root of the archive file</licenseComments>
        <summary>SPDX Translator utility</summary>
        <licenseInfoFromFiles rdf:resource="http://spdx.org/licenses/MPL-1.1"/>
        <externalRef>
          <ExternalRef>
            <referenceCategory rdf:resource="http://spdx.org/rdf/terms#referenceCategory_packageManager"/>
            <referenceType rdf:resource="http://spdx.org/rdf/references/maven-central"/>
            <referenceLocator>org.apache.commons:commons-lang:3.2.1</referenceLocator>
            <rdfs:comment>NIST National Vulnerability Database (NVD) describes security vulnerabilities (CVEs) which affect Vendor Product Version acmecorp:acmenator:6.6.6</rdfs:comment>
          </ExternalRef>
        </externalRef>
      </Package>
    </describesPackage>
    <rdfs:comment>This is a sample spreadsheet</rdfs:comment>
    <hasExtractedLicensingInfo rdf:nodeID="A4"/>
    <hasExtractedLicensingInfo rdf:nodeID="A5"/>
    <hasExtractedLicensingInfo rdf:nodeID="A3"/>
  </SpdxDocument>
</rdf:RDF>
