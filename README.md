# FHIR_Reporting_Tool

![](https://github.com/GisstHubana/FHIR_Reporting_Tool/blob/main/Diagramme/Webinterface_Reporting_Tool.png)

In dieser Projektarbeit im Rahmen des [Berufsbegleitenden Online-Master „Biomedizinische Informatik und Data Science“ der Hochschule Mannheim](https://www.master-bids.hs-mannheim.de/) wird eine Python-basierten FHIR-Reporting-Tools mit einer benutzerfreundlichen GUI zur Erstellung von Statistiken erstellt. Dies ermöglicht technisch weniger affinen Tool-Nutzern Klinikdaten, ohne zusätzliche Schulung, effizient zusammenzustellen, beispielsweise bezüglich der Anzahl erteilte Einwilligungen von Patienten in einer bestimmten Altersgruppe, und zu analysieren. Langfristig ist eine klinikinterne Integration für die Nutzung zu Forschungszwecken geplant.

Die Dokumentation des Projektes steht unter [FHIR_Reporting_Tool WIKI](https://github.com/GisstHubana/FHIR_Reporting_Tool/wiki) zur Verfügung.

Das Projekt entstand über mehrere Entwicklungsschritte: 
Ein vertiefter Einblick ist dem WIKI-Abschnitt [Projektmanagement](https://GisstHubana/FHIR_Reporting_Tool/wiki/Projektmanagment) zu entnehmen.

## Codeentwicklung
Der [Code](https://github.com/GisstHubana/FHIR_Reporting_Tool/blob/main/Code/fhir_reporting_tool.ipynb) wurde mit [Google Colaboratory](https://colab.research.google.com/?hl=de) auf Python-Basis geschrieben.

Die Erstellung des Webinterfaces erfolgte mit [Flask](https://flask.palletsprojects.com/en/3.0.x/) in Anlehnung an dieses [YouTube-Tutorial](https://www.youtube.com/watch?v=0dYsZt8-nXk&list=PLTUSGW0o2A2FgYB43QuL6wxnUM4dUr1n3).

## Hinweis zur Reproduzierbarkeit
Die Rohdaten können über [öffentliche Testserver des Kerndatensates der Medizininformatik Initiative](https://github.com/medizininformatik-initiative/kerndatensatz-testdaten) sowie als [Testdaten](https://github.com/medizininformatik-initiative/kerndatensatz-testdaten/tree/master/Test_Data) als  bezogen werden.
