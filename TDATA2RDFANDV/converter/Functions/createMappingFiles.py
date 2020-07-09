import json
import os

def createMappings(epwName):
    removeEpwSource()
    removeGroundTemperatureSource()
    removeLocationSource()
    removePeriodsSource()
    removeRMLMapping()
    createEpwSource(epwName)
    createGroundTemperatureSource(epwName)
    createLocationSource(epwName)
    createPeriodsSource(epwName)
    createRMLMapping(epwName)


def removeEpwSource():
    if os.path.exists("converter/MappingsEPWStorage/epw_data_source.json"):
        os.remove("converter/MappingsEPWStorage/epw_data_source.json")
        return
    else:
        return

def removeGroundTemperatureSource():
    if os.path.exists("converter/MappingsEPWStorage/groundTemperature_source.json"):
        os.remove("converter/MappingsEPWStorage/groundTemperature_source.json")
        return
    else:
        return

def removeLocationSource():
    if os.path.exists("converter/MappingsEPWStorage/location_source.json"):
        os.remove("converter/MappingsEPWStorage/location_source.json")
        return
    else:
        return

def removePeriodsSource():
    if os.path.exists("converter/MappingsEPWStorage/periods_source.json"):
        os.remove("converter/MappingsEPWStorage/periods_source.json")
        return
    else:
        return

def removeRMLMapping():
    if os.path.exists("converter/MappingsEPWStorage/mapping.rml"):
        os.remove("converter/MappingsEPWStorage/mapping.rml")
        return
    else:
        return


def createEpwSource(epwName):
    json_file = {}
    json_file['datasources'] = []
    json_file['datasources'].append({
          "id" : "EPW Values datasource",
          "type" : "JsonDatasource",
          "arguments" : ["$.epw[*]"],
          "connector"  : {
           "arguments" : ["../DataStorage/" + epwName + ".json"],
           "type" : "LocalFileConnector"
          }
        })
    document = open("converter/MappingsEPWStorage/epw_data_source.json", "w")
    json.dump(json_file, document, indent=4)

    document.close()

def createGroundTemperatureSource(epwName):
    json_file = {}
    json_file['datasources'] = []
    json_file['datasources'].append({
        "id" : "EPW Values groundTemperatures",
        "type" : "JsonDatasource",
        "arguments" : ["$.groundTemperatures[*]"],
        "connector"  : {
         "arguments" : ["../DataStorage/" + epwName + ".json"],
         "type" : "LocalFileConnector"
        }
      })
    document = open("converter/MappingsEPWStorage/groundTemperature_source.json", "w")
    json.dump(json_file, document, indent=4)
    document.close()



def createLocationSource(epwName):
    json_file = {}
    json_file['datasources'] = []
    json_file['datasources'].append({
          "id" : "EPW Values location",
          "type" : "JsonDatasource",
          "arguments" : ["$.location[*]"],
          "connector"  : {
           "arguments" : ["../DataStorage/" + epwName + ".json"],
           "type" : "LocalFileConnector"
          }
        })
    document = open("converter/MappingsEPWStorage/location_source.json", "w")
    json.dump(json_file, document, indent=4)
    document.close()

def createPeriodsSource(epwName):
    json_file = {}
    json_file['datasources'] = []
    json_file['datasources'].append({
          "id" : "EPW Values periods",
          "type" : "JsonDatasource",
          "arguments" : ["$.typical_extremePeriods[*]"],
          "connector"  : {
           "arguments" : ["../DataStorage/" + epwName + ".json"],
           "type" : "LocalFileConnector"
          }
        })
    document = open("converter/MappingsEPWStorage/periods_source.json", "w")
    json.dump(json_file, document, indent=4)
    document.close()


def createRMLMapping(epwName):
    document = open("converter/MappingsEPWStorage/mapping.rml", "w")
    document.write(
        """
        @prefix rr: <http://www.w3.org/ns/r2rml#>.
@prefix rml: <http://semweb.mmlab.be/ns/rml#>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix ql: <http://semweb.mmlab.be/ns/ql#>.
@prefix map: <http://mapping.example.com/>.

map:map_AerosolOpticalDepth_0 rml:logicalSource map:source_42;
    a rr:TriplesMap;
    rdfs:label "AerosolOpticalDepth";
    rr:subjectMap map:s_42;
    rr:predicateObjectMap map:pom_126.
map:map_AerosolOpticalDepthMeasurement_0 rml:logicalSource map:source_43;
    a rr:TriplesMap;
    rdfs:label "AerosolOpticalDepthMeasurement";
    rr:subjectMap map:s_43;
    rr:predicateObjectMap map:pom_127, map:pom_128, map:pom_129, map:pom_130, map:pom_131.
map:map_AtmosphericStationPressure_0 rml:logicalSource map:source_6;
    a rr:TriplesMap;
    rdfs:label "AtmosphericStationPressure";
    rr:subjectMap map:s_6;
    rr:predicateObjectMap map:pom_18.
map:map_AtmosphericStationPressureMeasurement_0 rml:logicalSource map:source_7;
    a rr:TriplesMap;
    rdfs:label "AtmosphericStationPressureMeasurement";
    rr:subjectMap map:s_7;
    rr:predicateObjectMap map:pom_19, map:pom_20, map:pom_21, map:pom_22, map:pom_23.
map:map_CeilingHeight_0 rml:logicalSource map:source_38;
    a rr:TriplesMap;
    rdfs:label "CeilingHeight";
    rr:subjectMap map:s_38;
    rr:predicateObjectMap map:pom_114.
map:map_CeilingHeightMeasurement_0 rml:logicalSource map:source_39;
    a rr:TriplesMap;
    rdfs:label "CeilingHeightMeasurement";
    rr:subjectMap map:s_39;
    rr:predicateObjectMap map:pom_115, map:pom_116, map:pom_117, map:pom_118, map:pom_119.
map:map_DaysSinceLastSnowfall_0 rml:logicalSource map:source_46;
    a rr:TriplesMap;
    rdfs:label "DaysSinceLastSnowfall";
    rr:subjectMap map:s_46;
    rr:predicateObjectMap map:pom_138.
map:map_DaysSinceLastSnowfallMeasurement_0 rml:logicalSource map:source_47;
    a rr:TriplesMap;
    rdfs:label "DaysSinceLastSnowfallMeasurement";
    rr:subjectMap map:s_47;
    rr:predicateObjectMap map:pom_139, map:pom_140, map:pom_141, map:pom_142, map:pom_143.
map:map_DewPointTemperature_0 rml:logicalSource map:source_2;
    a rr:TriplesMap;
    rdfs:label "DewPointTemperature";
    rr:subjectMap map:s_2;
    rr:predicateObjectMap map:pom_6.
map:map_DewPointTemperatureMeasurement_0 rml:logicalSource map:source_3;
    a rr:TriplesMap;
    rdfs:label "DewPointTemperatureMeasurement";
    rr:subjectMap map:s_3;
    rr:predicateObjectMap map:pom_7, map:pom_8, map:pom_9, map:pom_10, map:pom_11.
map:map_DiffuseHorizontalIlluminance_0 rml:logicalSource map:source_24;
    a rr:TriplesMap;
    rdfs:label "DiffuseHorizontalIlluminance";
    rr:subjectMap map:s_24;
    rr:predicateObjectMap map:pom_72.
map:map_DiffuseHorizontalIlluminanceMeasurement_0 rml:logicalSource map:source_25;
    a rr:TriplesMap;
    rdfs:label "DiffuseHorizontalIlluminanceMeasurement";
    rr:subjectMap map:s_25;
    rr:predicateObjectMap map:pom_73, map:pom_74, map:pom_75, map:pom_76, map:pom_77.
map:map_DiffuseHorizontalRadiation_0 rml:logicalSource map:source_18;
    a rr:TriplesMap;
    rdfs:label "DiffuseHorizontalRadiation";
    rr:subjectMap map:s_18;
    rr:predicateObjectMap map:pom_54.
map:map_DiffuseHorizontalRadiationMeasurement_0 rml:logicalSource map:source_19;
    a rr:TriplesMap;
    rdfs:label "DiffuseHorizontalRadiationMeasurement";
    rr:subjectMap map:s_19;
    rr:predicateObjectMap map:pom_55, map:pom_56, map:pom_57, map:pom_58, map:pom_59.
map:map_DirectNormalIlluminance_0 rml:logicalSource map:source_22;
    a rr:TriplesMap;
    rdfs:label "DirectNormalIlluminance";
    rr:subjectMap map:s_22;
    rr:predicateObjectMap map:pom_66.
map:map_DirectNormalIlluminanceMeasurement_0 rml:logicalSource map:source_23;
    a rr:TriplesMap;
    rdfs:label "DirectNormalIlluminanceMeasurement";
    rr:subjectMap map:s_23;
    rr:predicateObjectMap map:pom_67, map:pom_68, map:pom_69, map:pom_70, map:pom_71.
map:map_DirectNormalRadiation_0 rml:logicalSource map:source_16;
    a rr:TriplesMap;
    rdfs:label "DirectNormalRadiation";
    rr:subjectMap map:s_16;
    rr:predicateObjectMap map:pom_48.
map:map_DirectNormalRadiationMeasurement_0 rml:logicalSource map:source_17;
    a rr:TriplesMap;
    rdfs:label "DirectNormalRadiationMeasurement";
    rr:subjectMap map:s_17;
    rr:predicateObjectMap map:pom_49, map:pom_50, map:pom_51, map:pom_52, map:pom_53.
map:map_DryBulbTemperature_0 rml:logicalSource map:source_0;
    a rr:TriplesMap;
    rdfs:label "DryBulbTemperature";
    rr:subjectMap map:s_0;
    rr:predicateObjectMap map:pom_0.
map:map_DryBulbTemperatureMeasurement_0 rml:logicalSource map:source_1;
    a rr:TriplesMap;
    rdfs:label "DryBulbTemperatureMeasurement";
    rr:subjectMap map:s_1;
    rr:predicateObjectMap map:pom_1, map:pom_2, map:pom_3, map:pom_4, map:pom_5.
map:map_EPWName_0 rml:logicalSource map:source_52;
    a rr:TriplesMap;
    rdfs:label "EPWName";
    rr:subjectMap map:s_52;
    rr:predicateObjectMap map:pom_156, map:pom_157, map:pom_158, map:pom_159, map:pom_160, map:pom_161, map:pom_162, map:pom_163, map:pom_164, map:pom_165, map:pom_166, map:pom_167, map:pom_168, map:pom_169, map:pom_170, map:pom_171, map:pom_172, map:pom_173, map:pom_174, map:pom_175, map:pom_176, map:pom_177, map:pom_178, map:pom_179, map:pom_180, map:pom_181, map:pom_182.
map:map_ExtraterrestrialDirectNormalRadiation_0 rml:logicalSource map:source_10;
    a rr:TriplesMap;
    rdfs:label "ExtraterrestrialDirectNormalRadiation";
    rr:subjectMap map:s_10;
    rr:predicateObjectMap map:pom_30.
map:map_ExtraterrestrialDirectNormalRadiationMeasurement_0 rml:logicalSource map:source_11;
    a rr:TriplesMap;
    rdfs:label "ExtraterrestrialDirectNormalRadiationMeasurement";
    rr:subjectMap map:s_11;
    rr:predicateObjectMap map:pom_31, map:pom_32, map:pom_33, map:pom_34, map:pom_35.
map:map_ExtraterrestrialHorizontalRadiation_0 rml:logicalSource map:source_8;
    a rr:TriplesMap;
    rdfs:label "ExtraterrestrialHorizontalRadiation";
    rr:subjectMap map:s_8;
    rr:predicateObjectMap map:pom_24.
map:map_ExtraterrestrialHorizontalRadiationMeasurement_0 rml:logicalSource map:source_9;
    a rr:TriplesMap;
    rdfs:label "ExtraterrestrialHorizontalRadiationMeasurement";
    rr:subjectMap map:s_9;
    rr:predicateObjectMap map:pom_25, map:pom_26, map:pom_27, map:pom_28, map:pom_29.
map:map_GlobalHorizontalIlluminance_0 rml:logicalSource map:source_20;
    a rr:TriplesMap;
    rdfs:label "GlobalHorizontalIlluminance";
    rr:subjectMap map:s_20;
    rr:predicateObjectMap map:pom_60.
map:map_GlobalHorizontalIlluminanceMeasurement_0 rml:logicalSource map:source_21;
    a rr:TriplesMap;
    rdfs:label "GlobalHorizontalIlluminanceMeasurement";
    rr:subjectMap map:s_21;
    rr:predicateObjectMap map:pom_61, map:pom_62, map:pom_63, map:pom_64, map:pom_65.
map:map_GlobalHorizontalRadiation_0 rml:logicalSource map:source_14;
    a rr:TriplesMap;
    rdfs:label "GlobalHorizontalRadiation";
    rr:subjectMap map:s_14;
    rr:predicateObjectMap map:pom_42.
map:map_GlobalHorizontalRadiationMeasurement_0 rml:logicalSource map:source_15;
    a rr:TriplesMap;
    rdfs:label "GlobalHorizontalRadiationMeasurement";
    rr:subjectMap map:s_15;
    rr:predicateObjectMap map:pom_43, map:pom_44, map:pom_45, map:pom_46, map:pom_47.
map:map_GroundConductivity_0 rml:logicalSource map:source_54;
    a rr:TriplesMap;
    rdfs:label "GroundConductivity";
    rr:subjectMap map:s_54;
    rr:predicateObjectMap map:pom_185, map:pom_186.
map:map_GroundDensity_0 rml:logicalSource map:source_55;
    a rr:TriplesMap;
    rdfs:label "GroundDensity";
    rr:subjectMap map:s_55;
    rr:predicateObjectMap map:pom_187, map:pom_188.
map:map_GroundSpecificHeat_0 rml:logicalSource map:source_56;
    a rr:TriplesMap;
    rdfs:label "GroundSpecificHeat";
    rr:subjectMap map:s_56;
    rr:predicateObjectMap map:pom_189, map:pom_190.
map:map_GroundTemperature_0 rml:logicalSource map:source_57;
    a rr:TriplesMap;
    rdfs:label "GroundTemperature";
    rr:subjectMap map:s_57;
    rr:predicateObjectMap map:pom_191, map:pom_192.
map:map_GroundTemperatureDepth_0 rml:logicalSource map:source_53;
    a rr:TriplesMap;
    rdfs:label "GroundTemperatureDepth";
    rr:subjectMap map:s_53;
    rr:predicateObjectMap map:pom_183, map:pom_184.
map:map_HorizontalInfraredRadiationIntensity_0 rml:logicalSource map:source_12;
    a rr:TriplesMap;
    rdfs:label "HorizontalInfraredRadiationIntensity";
    rr:subjectMap map:s_12;
    rr:predicateObjectMap map:pom_36.
map:map_HorizontalInfraredRadiationIntensityMeasurement_0 rml:logicalSource map:source_13;
    a rr:TriplesMap;
    rdfs:label "HorizontalInfraredRadiationIntensityMeasurement";
    rr:subjectMap map:s_13;
    rr:predicateObjectMap map:pom_37, map:pom_38, map:pom_39, map:pom_40, map:pom_41.
map:map_LiquidPrecipitationDepth_0 rml:logicalSource map:source_48;
    a rr:TriplesMap;
    rdfs:label "LiquidPrecipitationDepth";
    rr:subjectMap map:s_48;
    rr:predicateObjectMap map:pom_144.
map:map_LiquidPrecipitationDepthMeasurement_0 rml:logicalSource map:source_49;
    a rr:TriplesMap;
    rdfs:label "LiquidPrecipitationDepthMeasurement";
    rr:subjectMap map:s_49;
    rr:predicateObjectMap map:pom_145, map:pom_146, map:pom_147, map:pom_148, map:pom_149.
map:map_LiquidPrecipitationQuantity_0 rml:logicalSource map:source_50;
    a rr:TriplesMap;
    rdfs:label "LiquidPrecipitationQuantity";
    rr:subjectMap map:s_50;
    rr:predicateObjectMap map:pom_150.
map:map_LiquidPrecipitationQuantityMeasurement_0 rml:logicalSource map:source_51;
    a rr:TriplesMap;
    rdfs:label "LiquidPrecipitationQuantityMeasurement";
    rr:subjectMap map:s_51;
    rr:predicateObjectMap map:pom_151, map:pom_152, map:pom_153, map:pom_154, map:pom_155.
map:map_Location_0 rml:logicalSource map:source_58;
    a rr:TriplesMap;
    rdfs:label "Location";
    rr:subjectMap map:s_58;
    rr:predicateObjectMap map:pom_193, map:pom_194, map:pom_195.
map:map_OpaqueSkyCover_0 rml:logicalSource map:source_34;
    a rr:TriplesMap;
    rdfs:label "OpaqueSkyCover";
    rr:subjectMap map:s_34;
    rr:predicateObjectMap map:pom_102.
map:map_OpaqueSkyCoverMeasurement_0 rml:logicalSource map:source_35;
    a rr:TriplesMap;
    rdfs:label "OpaqueSkyCoverMeasurement";
    rr:subjectMap map:s_35;
    rr:predicateObjectMap map:pom_103, map:pom_104, map:pom_105, map:pom_106, map:pom_107.
map:map_Periods_0 rml:logicalSource map:source_60;
    a rr:TriplesMap;
    rdfs:label "Periods";
    rr:subjectMap map:s_60;
    rr:predicateObjectMap map:pom_199.
map:map_PeriodsEPWName_0 rml:logicalSource map:source_62;
    a rr:TriplesMap;
    rdfs:label "PeriodsEPWName";
    rr:subjectMap map:s_62;
    rr:predicateObjectMap map:pom_203.
map:map_PeriodsSeason_0 rml:logicalSource map:source_61;
    a rr:TriplesMap;
    rdfs:label "PeriodsSeason";
    rr:subjectMap map:s_61;
    rr:predicateObjectMap map:pom_200, map:pom_201, map:pom_202.
map:map_Point_0 rml:logicalSource map:source_59;
    a rr:TriplesMap;
    rdfs:label "Point";
    rr:subjectMap map:s_59;
    rr:predicateObjectMap map:pom_196, map:pom_197, map:pom_198.
map:map_PrecipitableWater_0 rml:logicalSource map:source_40;
    a rr:TriplesMap;
    rdfs:label "PrecipitableWater";
    rr:subjectMap map:s_40;
    rr:predicateObjectMap map:pom_120.
map:map_PrecipitableWaterMeasurement_0 rml:logicalSource map:source_41;
    a rr:TriplesMap;
    rdfs:label "PrecipitableWaterMeasurement";
    rr:subjectMap map:s_41;
    rr:predicateObjectMap map:pom_121, map:pom_122, map:pom_123, map:pom_124, map:pom_125.
map:map_RelativeHumidity_0 rml:logicalSource map:source_4;
    a rr:TriplesMap;
    rdfs:label "RelativeHumidity";
    rr:subjectMap map:s_4;
    rr:predicateObjectMap map:pom_12.
map:map_RelativeHumidityMeasurement_0 rml:logicalSource map:source_5;
    a rr:TriplesMap;
    rdfs:label "RelativeHumidityMeasurement";
    rr:subjectMap map:s_5;
    rr:predicateObjectMap map:pom_13, map:pom_14, map:pom_15, map:pom_16, map:pom_17.
map:map_SnowDepth_0 rml:logicalSource map:source_44;
    a rr:TriplesMap;
    rdfs:label "SnowDepth";
    rr:subjectMap map:s_44;
    rr:predicateObjectMap map:pom_132.
map:map_SnowDepthMeasurement_0 rml:logicalSource map:source_45;
    a rr:TriplesMap;
    rdfs:label "SnowDepthMeasurement";
    rr:subjectMap map:s_45;
    rr:predicateObjectMap map:pom_133, map:pom_134, map:pom_135, map:pom_136, map:pom_137.
map:map_TotalSkyCover_0 rml:logicalSource map:source_32;
    a rr:TriplesMap;
    rdfs:label "TotalSkyCover";
    rr:subjectMap map:s_32;
    rr:predicateObjectMap map:pom_96.
map:map_TotalSkyCoverMeasurement_0 rml:logicalSource map:source_33;
    a rr:TriplesMap;
    rdfs:label "TotalSkyCoverMeasurement";
    rr:subjectMap map:s_33;
    rr:predicateObjectMap map:pom_97, map:pom_98, map:pom_99, map:pom_100, map:pom_101.
map:map_Visibility_0 rml:logicalSource map:source_36;
    a rr:TriplesMap;
    rdfs:label "Visibility";
    rr:subjectMap map:s_36;
    rr:predicateObjectMap map:pom_108.
map:map_VisibilityMeasurement_0 rml:logicalSource map:source_37;
    a rr:TriplesMap;
    rdfs:label "VisibilityMeasurement";
    rr:subjectMap map:s_37;
    rr:predicateObjectMap map:pom_109, map:pom_110, map:pom_111, map:pom_112, map:pom_113.
map:map_WindDirection_0 rml:logicalSource map:source_28;
    a rr:TriplesMap;
    rdfs:label "WindDirection";
    rr:subjectMap map:s_28;
    rr:predicateObjectMap map:pom_84.
map:map_WindDirectionMeasurement_0 rml:logicalSource map:source_29;
    a rr:TriplesMap;
    rdfs:label "WindDirectionMeasurement";
    rr:subjectMap map:s_29;
    rr:predicateObjectMap map:pom_85, map:pom_86, map:pom_87, map:pom_88, map:pom_89.
map:map_WindSpeed_0 rml:logicalSource map:source_30;
    a rr:TriplesMap;
    rdfs:label "WindSpeed";
    rr:subjectMap map:s_30;
    rr:predicateObjectMap map:pom_90.
map:map_WindSpeedMeasurement_0 rml:logicalSource map:source_31;
    a rr:TriplesMap;
    rdfs:label "WindSpeedMeasurement";
    rr:subjectMap map:s_31;
    rr:predicateObjectMap map:pom_91, map:pom_92, map:pom_93, map:pom_94, map:pom_95.
map:map_ZenithLuminance_0 rml:logicalSource map:source_26;
    a rr:TriplesMap;
    rdfs:label "ZenithLuminance";
    rr:subjectMap map:s_26;
    rr:predicateObjectMap map:pom_78.
map:map_ZenithLuminanceMeasurement_0 rml:logicalSource map:source_27;
    a rr:TriplesMap;
    rdfs:label "ZenithLuminanceMeasurement";
    rr:subjectMap map:s_27;
    rr:predicateObjectMap map:pom_79, map:pom_80, map:pom_81, map:pom_82, map:pom_83.
map:om_0 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DryBulbTemperatureMeasurement";
    rr:termType rr:IRI.
map:om_1 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_10 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/degreeCelsius";
    rr:termType rr:Literal.
map:om_100 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#tenthsOfCoverage";
    rr:termType rr:Literal.
map:om_101 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_102 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/OpaqueSkyCoverMeasurement";
    rr:termType rr:IRI.
map:om_103 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_104 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_105 a rr:ObjectMap;
    rml:reference "OpaqueSkyCover";
    rr:termType rr:Literal.
map:om_106 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#tenthsOfCoverage";
    rr:termType rr:Literal.
map:om_107 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_108 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/VisibilityMeasurement";
    rr:termType rr:IRI.
map:om_109 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_11 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_110 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_111 a rr:ObjectMap;
    rml:reference "Visibility";
    rr:termType rr:Literal.
map:om_112 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/kilometre";
    rr:termType rr:Literal.
map:om_113 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_114 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/CeilingHeightMeasurement";
    rr:termType rr:IRI.
map:om_115 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_116 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_117 a rr:ObjectMap;
    rml:reference "CeilingHeight";
    rr:termType rr:Literal.
map:om_118 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/metre";
    rr:termType rr:Literal.
map:om_119 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_12 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/RelativeHumidityMeasurement";
    rr:termType rr:IRI.
map:om_120 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/PrecipitableWaterMeasurement";
    rr:termType rr:IRI.
map:om_121 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_122 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_123 a rr:ObjectMap;
    rml:reference "PrecipitableWater";
    rr:termType rr:Literal.
map:om_124 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/millimetre";
    rr:termType rr:Literal.
map:om_125 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_126 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AerosolOpticalDepthMeasurement";
    rr:termType rr:IRI.
map:om_127 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_128 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_129 a rr:ObjectMap;
    rml:reference "AerosolOpticalDepth";
    rr:termType rr:Literal.
map:om_13 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_130 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#thousandths";
    rr:termType rr:Literal.
map:om_131 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_132 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/SnowDepthMeasurement";
    rr:termType rr:IRI.
map:om_133 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_134 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_135 a rr:ObjectMap;
    rml:reference "SnowDepth";
    rr:termType rr:Literal.
map:om_136 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/centimetre";
    rr:termType rr:Literal.
map:om_137 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_138 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DaysSinceLastSnowfallMeasurement";
    rr:termType rr:IRI.
map:om_139 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_14 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_140 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_141 a rr:ObjectMap;
    rml:reference "DaysSinceLastSnowfall";
    rr:termType rr:Literal.
map:om_142 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/day";
    rr:termType rr:Literal.
map:om_143 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_144 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/LiquidPrecipitationDepthMeasurement";
    rr:termType rr:IRI.
map:om_145 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_146 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_147 a rr:ObjectMap;
    rml:reference "LiquidPrecipitationDepth";
    rr:termType rr:Literal.
map:om_148 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/millimetre";
    rr:termType rr:Literal.
map:om_149 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_15 a rr:ObjectMap;
    rml:reference "RelativeHumidity";
    rr:termType rr:Literal.
map:om_150 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/LiquidPrecipitationQuantityMeasurement";
    rr:termType rr:IRI.
map:om_151 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_152 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_153 a rr:ObjectMap;
    rml:reference "LiquidPrecipitationQuantity";
    rr:termType rr:Literal.
map:om_154 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/hour";
    rr:termType rr:Literal.
map:om_155 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_156 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DryBulbTemperatureMeasurement";
    rr:termType rr:IRI.
map:om_157 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DewPointTemperatureMeasurement";
    rr:termType rr:IRI.
map:om_158 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/RelativeHumidityMeasurement";
    rr:termType rr:IRI.
map:om_159 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AtmosphericStationPressureMeasurement";
    rr:termType rr:IRI.
map:om_16 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/percent";
    rr:termType rr:Literal.
map:om_160 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ExtraterrestrialHorizontalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_161 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ExtraterrestrialDirectNormalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_162 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/HorizontalInfraredRadiationIntensityMeasurement";
    rr:termType rr:IRI.
map:om_163 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/GlobalHorizontalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_164 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DirectNormalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_165 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DiffuseHorizontalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_166 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/GlobalHorizontalIlluminanceMeasurement";
    rr:termType rr:IRI.
map:om_167 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DirectNormalIlluminanceMeasurement";
    rr:termType rr:IRI.
map:om_168 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DiffuseHorizontalIlluminanceMeasurement";
    rr:termType rr:IRI.
map:om_169 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ZenithLuminanceMeasurement";
    rr:termType rr:IRI.
map:om_17 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_170 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/WindDirectionMeasurement";
    rr:termType rr:IRI.
map:om_171 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/WindSpeedMeasurement";
    rr:termType rr:IRI.
map:om_172 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/TotalSkyCoverMeasurement";
    rr:termType rr:IRI.
map:om_173 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/OpaqueSkyCoverMeasurement";
    rr:termType rr:IRI.
map:om_174 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/VisibilityMeasurement";
    rr:termType rr:IRI.
map:om_175 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/CeilingHeightMeasurement";
    rr:termType rr:IRI.
map:om_176 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/PrecipitableWaterMeasurement";
    rr:termType rr:IRI.
map:om_177 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AerosolOpticalDepthMeasurement";
    rr:termType rr:IRI.
map:om_178 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/SnowDepthMeasurement";
    rr:termType rr:IRI.
map:om_179 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DaysSinceLastSnowfallMeasurement";
    rr:termType rr:IRI.
map:om_18 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AtmosphericStationPressureMeasurement";
    rr:termType rr:IRI.
map:om_180 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AlbedoMeasurement";
    rr:termType rr:IRI.
map:om_181 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/LiquidPrecipitationDepthMeasurement";
    rr:termType rr:IRI.
map:om_182 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/LiquidPrecipitationQuantityMeasurement";
    rr:termType rr:IRI.
map:om_183 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/metre";
    rr:termType rr:IRI.
map:om_184 a rr:ObjectMap;
    rml:reference "groundTemperatureDepth";
    rr:termType rr:Literal.
map:om_185 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/wattPerMetreKelvin";
    rr:termType rr:IRI.
map:om_186 a rr:ObjectMap;
    rml:reference "groundConductivity";
    rr:termType rr:Literal.
map:om_187 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/kilogramPerCubicmetre";
    rr:termType rr:IRI.
map:om_188 a rr:ObjectMap;
    rml:reference "groundDensity";
    rr:termType rr:Literal.
map:om_189 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/joulePerKiligram";
    rr:termType rr:IRI.
map:om_19 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_190 a rr:ObjectMap;
    rml:reference "groundSpecificHeat";
    rr:termType rr:Literal.
map:om_191 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/degreeCelsius";
    rr:termType rr:IRI.
map:om_192 a rr:ObjectMap;
    rr:template "January:{january} - February:{february} - March:{march} - April:{april} - May:{may} - June:{june} - July:{july} - August:{august} - September{september} - October:{october} - November:{november} - December:{december}";
    rr:termType rr:Literal.
map:om_193 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/city/{city}";
    rr:termType rr:IRI.
map:om_194 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/country/{country}";
    rr:termType rr:IRI.
map:om_195 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/spatialThing/Point";
    rr:termType rr:IRI.
map:om_196 a rr:ObjectMap;
    rml:reference "lat";
    rr:termType rr:Literal.
map:om_197 a rr:ObjectMap;
    rml:reference "long";
    rr:termType rr:Literal.
map:om_198 a rr:ObjectMap;
    rml:reference "alt";
    rr:termType rr:Literal.
map:om_199 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/{typeOfPeriod}/{season}";
    rr:termType rr:Literal.
map:om_2 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_20 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_200 a rr:ObjectMap;
    rml:reference "firstDate";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_201 a rr:ObjectMap;
    rml:reference "lastDate";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_202 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:Literal.
map:om_203 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/{typeOfPeriod}/{season}";
    rr:termType rr:Literal.
map:om_21 a rr:ObjectMap;
    rml:reference "AtmosphericStationPressure";
    rr:termType rr:Literal.
map:om_22 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/pascal";
    rr:termType rr:Literal.
map:om_23 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_24 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ExtraterrestrialHorizontalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_25 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_26 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_27 a rr:ObjectMap;
    rml:reference "ExtraterrestrialHorizontalRadiation";
    rr:termType rr:Literal.
map:om_28 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#wattHourPerSquareMetre";
    rr:termType rr:Literal.
map:om_29 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_3 a rr:ObjectMap;
    rml:reference "DryBulbTemperature";
    rr:termType rr:Literal.
map:om_30 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ExtraterrestrialDirectNormalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_31 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_32 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_33 a rr:ObjectMap;
    rml:reference "ExtraterrestrialDirectNormalRadiation";
    rr:termType rr:Literal.
map:om_34 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#wattHourPerSquareMetre";
    rr:termType rr:Literal.
map:om_35 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_36 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/HorizontalInfraredRadiationIntensityMeasurement";
    rr:termType rr:IRI.
map:om_37 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_38 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_39 a rr:ObjectMap;
    rml:reference "HorizontalInfraredRadiationIntensity";
    rr:termType rr:Literal.
map:om_4 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/degreeCelsius";
    rr:termType rr:Literal.
map:om_40 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#wattHourPerSquareMetre";
    rr:termType rr:Literal.
map:om_41 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_42 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/GlobalHorizontalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_43 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_44 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_45 a rr:ObjectMap;
    rml:reference "GlobalHorizontalRadiation";
    rr:termType rr:Literal.
map:om_46 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#wattHourPerSquareMetre";
    rr:termType rr:Literal.
map:om_47 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_48 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DirectNormalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_49 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_5 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_50 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_51 a rr:ObjectMap;
    rml:reference "DirectNormalRadiation";
    rr:termType rr:Literal.
map:om_52 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#wattHourPerSquareMetre";
    rr:termType rr:Literal.
map:om_53 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_54 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DiffuseHorizontalRadiationMeasurement";
    rr:termType rr:IRI.
map:om_55 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_56 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_57 a rr:ObjectMap;
    rml:reference "DiffuseHorizontalRadiation";
    rr:termType rr:Literal.
map:om_58 a rr:ObjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#wattHourPerSquareMetre";
    rr:termType rr:Literal.
map:om_59 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_6 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DewPointTemperatureMeasurement";
    rr:termType rr:IRI.
map:om_60 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/GlobalHorizontalIlluminanceMeasurement";
    rr:termType rr:IRI.
map:om_61 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_62 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_63 a rr:ObjectMap;
    rml:reference "GlobalHorizontalIlluminance";
    rr:termType rr:Literal.
map:om_64 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/lux";
    rr:termType rr:Literal.
map:om_65 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_66 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DirectNormalIlluminanceMeasurement";
    rr:termType rr:IRI.
map:om_67 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_68 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_69 a rr:ObjectMap;
    rml:reference "DirectNormalIlluminance";
    rr:termType rr:Literal.
map:om_7 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_70 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/lux";
    rr:termType rr:Literal.
map:om_71 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_72 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DiffuseHorizontalIlluminanceMeasurement";
    rr:termType rr:IRI.
map:om_73 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_74 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_75 a rr:ObjectMap;
    rml:reference "DiffuseHorizontalIlluminance";
    rr:termType rr:Literal.
map:om_76 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/lux";
    rr:termType rr:Literal.
map:om_77 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_78 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ZenithLuminanceMeasurement";
    rr:termType rr:IRI.
map:om_79 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_8 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_80 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_81 a rr:ObjectMap;
    rml:reference "ZenithLuminance";
    rr:termType rr:Literal.
map:om_82 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/candelaPerSquareMetre";
    rr:termType rr:Literal.
map:om_83 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_84 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/WindDirectionMeasurement";
    rr:termType rr:IRI.
map:om_85 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_86 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_87 a rr:ObjectMap;
    rml:reference "WindDirection";
    rr:termType rr:Literal.
map:om_88 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/degree";
    rr:termType rr:Literal.
map:om_89 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_9 a rr:ObjectMap;
    rml:reference "DewPointTemperature";
    rr:termType rr:Literal.
map:om_90 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/WindSpeedMeasurement";
    rr:termType rr:IRI.
map:om_91 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_92 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_93 a rr:ObjectMap;
    rml:reference "WindSpeed";
    rr:termType rr:Literal.
map:om_94 a rr:ObjectMap;
    rr:constant "http://www.ontology-of-units-of-measure.org/resource/om-2/metrePerSecond-Time";
    rr:termType rr:Literal.
map:om_95 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}";
    rr:termType rr:IRI.
map:om_96 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/TotalSkyCoverMeasurement";
    rr:termType rr:IRI.
map:om_97 a rr:ObjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device";
    rr:termType rr:IRI.
map:om_98 a rr:ObjectMap;
    rr:template "{Year}-{Month}-{Day}-{Hour}";
    rr:termType rr:Literal;
    rr:datatype <http://www.w3.org/2001/XMLSchema#dateTime>.
map:om_99 a rr:ObjectMap;
    rml:reference "TotalSkyCover";
    rr:termType rr:Literal.
map:pm_0 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_1 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_10 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_100 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_101 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_102 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_103 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_104 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_105 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_106 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_107 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_108 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_109 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_11 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_110 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_111 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_112 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_113 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_114 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_115 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_116 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_117 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_118 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_119 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_12 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_120 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_121 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_122 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_123 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_124 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_125 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_126 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_127 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_128 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_129 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_13 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_130 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_131 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_132 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_133 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_134 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_135 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_136 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_137 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_138 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_139 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_14 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_140 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_141 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_142 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_143 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_144 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_145 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_146 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_147 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_148 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_149 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_15 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_150 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_151 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_152 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_153 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_154 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_155 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_156 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_157 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_158 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_159 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_16 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_160 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_161 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_162 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_163 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_164 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_165 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_166 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_167 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_168 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_169 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_17 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_170 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_171 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_172 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_173 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_174 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_175 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_176 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_177 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_178 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_179 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_18 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_180 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_181 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_182 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_183 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_184 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_185 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_186 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_187 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_188 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_189 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_19 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_190 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_191 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_192 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_193 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#locatedIn>.
map:pm_194 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#locatedIn>.
map:pm_195 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#locatedIn>.
map:pm_196 a rr:PredicateMap;
    rr:constant <http://www.w3.org/2003/01/geo/wgs84_pos#lat>.
map:pm_197 a rr:PredicateMap;
    rr:constant <http://www.w3.org/2003/01/geo/wgs84_pos#long>.
map:pm_198 a rr:PredicateMap;
    rr:constant <http://www.w3.org/2003/01/geo/wgs84_pos#alt>.
map:pm_199 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/resource/weather/observedInSeason>.
map:pm_2 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_20 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_200 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#firstDate>.
map:pm_201 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#lastDate>.
map:pm_202 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_203 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinedBy>.
map:pm_21 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_22 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_23 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_24 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_25 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_26 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_27 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_28 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_29 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_3 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_30 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_31 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_32 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_33 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_34 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_35 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_36 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_37 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_38 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_39 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_4 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_40 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_41 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_42 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_43 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_44 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_45 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_46 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_47 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_48 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_49 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_5 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_50 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_51 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_52 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_53 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_54 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_55 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_56 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_57 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_58 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_59 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_6 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_60 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_61 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_62 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_63 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_64 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_65 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_66 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_67 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_68 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_69 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_7 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_70 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_71 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_72 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_73 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_74 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_75 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_76 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_77 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_78 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_79 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_8 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_80 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_81 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_82 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_83 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_84 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_85 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_86 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_87 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_88 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_89 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_9 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_90 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_91 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_92 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_93 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pm_94 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/isMeasuredIn>.
map:pm_95 a rr:PredicateMap;
    rr:constant <https://bimerr.iot.linkeddata.es/def/weather#isDefinitionOf>.
map:pm_96 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/relatesToMeasurement>.
map:pm_97 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/measurementMadeBy>.
map:pm_98 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasTimeStamp>.
map:pm_99 a rr:PredicateMap;
    rr:constant <https://saref.etsi.org/core/hasValue>.
map:pom_0 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_0;
    rr:objectMap map:om_0.
map:pom_1 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_1;
    rr:objectMap map:om_1.
map:pom_10 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_10;
    rr:objectMap map:om_10.
map:pom_100 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_100;
    rr:objectMap map:om_100.
map:pom_101 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_101;
    rr:objectMap map:om_101.
map:pom_102 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_102;
    rr:objectMap map:om_102.
map:pom_103 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_103;
    rr:objectMap map:om_103.
map:pom_104 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_104;
    rr:objectMap map:om_104.
map:pom_105 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_105;
    rr:objectMap map:om_105.
map:pom_106 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_106;
    rr:objectMap map:om_106.
map:pom_107 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_107;
    rr:objectMap map:om_107.
map:pom_108 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_108;
    rr:objectMap map:om_108.
map:pom_109 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_109;
    rr:objectMap map:om_109.
map:pom_11 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_11;
    rr:objectMap map:om_11.
map:pom_110 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_110;
    rr:objectMap map:om_110.
map:pom_111 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_111;
    rr:objectMap map:om_111.
map:pom_112 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_112;
    rr:objectMap map:om_112.
map:pom_113 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_113;
    rr:objectMap map:om_113.
map:pom_114 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_114;
    rr:objectMap map:om_114.
map:pom_115 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_115;
    rr:objectMap map:om_115.
map:pom_116 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_116;
    rr:objectMap map:om_116.
map:pom_117 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_117;
    rr:objectMap map:om_117.
map:pom_118 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_118;
    rr:objectMap map:om_118.
map:pom_119 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_119;
    rr:objectMap map:om_119.
map:pom_12 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_12;
    rr:objectMap map:om_12.
map:pom_120 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_120;
    rr:objectMap map:om_120.
map:pom_121 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_121;
    rr:objectMap map:om_121.
map:pom_122 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_122;
    rr:objectMap map:om_122.
map:pom_123 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_123;
    rr:objectMap map:om_123.
map:pom_124 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_124;
    rr:objectMap map:om_124.
map:pom_125 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_125;
    rr:objectMap map:om_125.
map:pom_126 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_126;
    rr:objectMap map:om_126.
map:pom_127 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_127;
    rr:objectMap map:om_127.
map:pom_128 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_128;
    rr:objectMap map:om_128.
map:pom_129 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_129;
    rr:objectMap map:om_129.
map:pom_13 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_13;
    rr:objectMap map:om_13.
map:pom_130 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_130;
    rr:objectMap map:om_130.
map:pom_131 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_131;
    rr:objectMap map:om_131.
map:pom_132 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_132;
    rr:objectMap map:om_132.
map:pom_133 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_133;
    rr:objectMap map:om_133.
map:pom_134 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_134;
    rr:objectMap map:om_134.
map:pom_135 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_135;
    rr:objectMap map:om_135.
map:pom_136 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_136;
    rr:objectMap map:om_136.
map:pom_137 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_137;
    rr:objectMap map:om_137.
map:pom_138 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_138;
    rr:objectMap map:om_138.
map:pom_139 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_139;
    rr:objectMap map:om_139.
map:pom_14 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_14;
    rr:objectMap map:om_14.
map:pom_140 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_140;
    rr:objectMap map:om_140.
map:pom_141 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_141;
    rr:objectMap map:om_141.
map:pom_142 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_142;
    rr:objectMap map:om_142.
map:pom_143 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_143;
    rr:objectMap map:om_143.
map:pom_144 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_144;
    rr:objectMap map:om_144.
map:pom_145 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_145;
    rr:objectMap map:om_145.
map:pom_146 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_146;
    rr:objectMap map:om_146.
map:pom_147 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_147;
    rr:objectMap map:om_147.
map:pom_148 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_148;
    rr:objectMap map:om_148.
map:pom_149 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_149;
    rr:objectMap map:om_149.
map:pom_15 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_15;
    rr:objectMap map:om_15.
map:pom_150 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_150;
    rr:objectMap map:om_150.
map:pom_151 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_151;
    rr:objectMap map:om_151.
map:pom_152 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_152;
    rr:objectMap map:om_152.
map:pom_153 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_153;
    rr:objectMap map:om_153.
map:pom_154 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_154;
    rr:objectMap map:om_154.
map:pom_155 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_155;
    rr:objectMap map:om_155.
map:pom_156 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_156;
    rr:objectMap map:om_156.
map:pom_157 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_157;
    rr:objectMap map:om_157.
map:pom_158 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_158;
    rr:objectMap map:om_158.
map:pom_159 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_159;
    rr:objectMap map:om_159.
map:pom_16 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_16;
    rr:objectMap map:om_16.
map:pom_160 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_160;
    rr:objectMap map:om_160.
map:pom_161 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_161;
    rr:objectMap map:om_161.
map:pom_162 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_162;
    rr:objectMap map:om_162.
map:pom_163 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_163;
    rr:objectMap map:om_163.
map:pom_164 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_164;
    rr:objectMap map:om_164.
map:pom_165 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_165;
    rr:objectMap map:om_165.
map:pom_166 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_166;
    rr:objectMap map:om_166.
map:pom_167 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_167;
    rr:objectMap map:om_167.
map:pom_168 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_168;
    rr:objectMap map:om_168.
map:pom_169 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_169;
    rr:objectMap map:om_169.
map:pom_17 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_17;
    rr:objectMap map:om_17.
map:pom_170 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_170;
    rr:objectMap map:om_170.
map:pom_171 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_171;
    rr:objectMap map:om_171.
map:pom_172 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_172;
    rr:objectMap map:om_172.
map:pom_173 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_173;
    rr:objectMap map:om_173.
map:pom_174 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_174;
    rr:objectMap map:om_174.
map:pom_175 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_175;
    rr:objectMap map:om_175.
map:pom_176 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_176;
    rr:objectMap map:om_176.
map:pom_177 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_177;
    rr:objectMap map:om_177.
map:pom_178 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_178;
    rr:objectMap map:om_178.
map:pom_179 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_179;
    rr:objectMap map:om_179.
map:pom_18 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_18;
    rr:objectMap map:om_18.
map:pom_180 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_180;
    rr:objectMap map:om_180.
map:pom_181 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_181;
    rr:objectMap map:om_181.
map:pom_182 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_182;
    rr:objectMap map:om_182.
map:pom_183 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_183;
    rr:objectMap map:om_183.
map:pom_184 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_184;
    rr:objectMap map:om_184.
map:pom_185 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_185;
    rr:objectMap map:om_185.
map:pom_186 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_186;
    rr:objectMap map:om_186.
map:pom_187 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_187;
    rr:objectMap map:om_187.
map:pom_188 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_188;
    rr:objectMap map:om_188.
map:pom_189 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_189;
    rr:objectMap map:om_189.
map:pom_19 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_19;
    rr:objectMap map:om_19.
map:pom_190 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_190;
    rr:objectMap map:om_190.
map:pom_191 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_191;
    rr:objectMap map:om_191.
map:pom_192 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_192;
    rr:objectMap map:om_192.
map:pom_193 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_193;
    rr:objectMap map:om_193.
map:pom_194 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_194;
    rr:objectMap map:om_194.
map:pom_195 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_195;
    rr:objectMap map:om_195.
map:pom_196 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_196;
    rr:objectMap map:om_196.
map:pom_197 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_197;
    rr:objectMap map:om_197.
map:pom_198 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_198;
    rr:objectMap map:om_198.
map:pom_199 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_199;
    rr:objectMap map:om_199.
map:pom_2 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_2;
    rr:objectMap map:om_2.
map:pom_20 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_20;
    rr:objectMap map:om_20.
map:pom_200 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_200;
    rr:objectMap map:om_200.
map:pom_201 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_201;
    rr:objectMap map:om_201.
map:pom_202 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_202;
    rr:objectMap map:om_202.
map:pom_203 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_203;
    rr:objectMap map:om_203.
map:pom_21 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_21;
    rr:objectMap map:om_21.
map:pom_22 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_22;
    rr:objectMap map:om_22.
map:pom_23 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_23;
    rr:objectMap map:om_23.
map:pom_24 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_24;
    rr:objectMap map:om_24.
map:pom_25 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_25;
    rr:objectMap map:om_25.
map:pom_26 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_26;
    rr:objectMap map:om_26.
map:pom_27 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_27;
    rr:objectMap map:om_27.
map:pom_28 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_28;
    rr:objectMap map:om_28.
map:pom_29 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_29;
    rr:objectMap map:om_29.
map:pom_3 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_3;
    rr:objectMap map:om_3.
map:pom_30 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_30;
    rr:objectMap map:om_30.
map:pom_31 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_31;
    rr:objectMap map:om_31.
map:pom_32 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_32;
    rr:objectMap map:om_32.
map:pom_33 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_33;
    rr:objectMap map:om_33.
map:pom_34 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_34;
    rr:objectMap map:om_34.
map:pom_35 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_35;
    rr:objectMap map:om_35.
map:pom_36 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_36;
    rr:objectMap map:om_36.
map:pom_37 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_37;
    rr:objectMap map:om_37.
map:pom_38 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_38;
    rr:objectMap map:om_38.
map:pom_39 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_39;
    rr:objectMap map:om_39.
map:pom_4 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_4;
    rr:objectMap map:om_4.
map:pom_40 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_40;
    rr:objectMap map:om_40.
map:pom_41 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_41;
    rr:objectMap map:om_41.
map:pom_42 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_42;
    rr:objectMap map:om_42.
map:pom_43 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_43;
    rr:objectMap map:om_43.
map:pom_44 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_44;
    rr:objectMap map:om_44.
map:pom_45 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_45;
    rr:objectMap map:om_45.
map:pom_46 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_46;
    rr:objectMap map:om_46.
map:pom_47 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_47;
    rr:objectMap map:om_47.
map:pom_48 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_48;
    rr:objectMap map:om_48.
map:pom_49 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_49;
    rr:objectMap map:om_49.
map:pom_5 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_5;
    rr:objectMap map:om_5.
map:pom_50 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_50;
    rr:objectMap map:om_50.
map:pom_51 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_51;
    rr:objectMap map:om_51.
map:pom_52 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_52;
    rr:objectMap map:om_52.
map:pom_53 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_53;
    rr:objectMap map:om_53.
map:pom_54 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_54;
    rr:objectMap map:om_54.
map:pom_55 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_55;
    rr:objectMap map:om_55.
map:pom_56 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_56;
    rr:objectMap map:om_56.
map:pom_57 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_57;
    rr:objectMap map:om_57.
map:pom_58 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_58;
    rr:objectMap map:om_58.
map:pom_59 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_59;
    rr:objectMap map:om_59.
map:pom_6 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_6;
    rr:objectMap map:om_6.
map:pom_60 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_60;
    rr:objectMap map:om_60.
map:pom_61 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_61;
    rr:objectMap map:om_61.
map:pom_62 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_62;
    rr:objectMap map:om_62.
map:pom_63 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_63;
    rr:objectMap map:om_63.
map:pom_64 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_64;
    rr:objectMap map:om_64.
map:pom_65 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_65;
    rr:objectMap map:om_65.
map:pom_66 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_66;
    rr:objectMap map:om_66.
map:pom_67 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_67;
    rr:objectMap map:om_67.
map:pom_68 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_68;
    rr:objectMap map:om_68.
map:pom_69 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_69;
    rr:objectMap map:om_69.
map:pom_7 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_7;
    rr:objectMap map:om_7.
map:pom_70 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_70;
    rr:objectMap map:om_70.
map:pom_71 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_71;
    rr:objectMap map:om_71.
map:pom_72 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_72;
    rr:objectMap map:om_72.
map:pom_73 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_73;
    rr:objectMap map:om_73.
map:pom_74 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_74;
    rr:objectMap map:om_74.
map:pom_75 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_75;
    rr:objectMap map:om_75.
map:pom_76 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_76;
    rr:objectMap map:om_76.
map:pom_77 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_77;
    rr:objectMap map:om_77.
map:pom_78 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_78;
    rr:objectMap map:om_78.
map:pom_79 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_79;
    rr:objectMap map:om_79.
map:pom_8 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_8;
    rr:objectMap map:om_8.
map:pom_80 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_80;
    rr:objectMap map:om_80.
map:pom_81 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_81;
    rr:objectMap map:om_81.
map:pom_82 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_82;
    rr:objectMap map:om_82.
map:pom_83 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_83;
    rr:objectMap map:om_83.
map:pom_84 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_84;
    rr:objectMap map:om_84.
map:pom_85 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_85;
    rr:objectMap map:om_85.
map:pom_86 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_86;
    rr:objectMap map:om_86.
map:pom_87 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_87;
    rr:objectMap map:om_87.
map:pom_88 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_88;
    rr:objectMap map:om_88.
map:pom_89 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_89;
    rr:objectMap map:om_89.
map:pom_9 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_9;
    rr:objectMap map:om_9.
map:pom_90 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_90;
    rr:objectMap map:om_90.
map:pom_91 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_91;
    rr:objectMap map:om_91.
map:pom_92 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_92;
    rr:objectMap map:om_92.
map:pom_93 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_93;
    rr:objectMap map:om_93.
map:pom_94 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_94;
    rr:objectMap map:om_94.
map:pom_95 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_95;
    rr:objectMap map:om_95.
map:pom_96 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_96;
    rr:objectMap map:om_96.
map:pom_97 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_97;
    rr:objectMap map:om_97.
map:pom_98 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_98;
    rr:objectMap map:om_98.
map:pom_99 a rr:PredicateObjectMap;
    rr:predicateMap map:pm_99;
    rr:objectMap map:om_99.
map:s_0 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DryBulbTemperature".
map:s_1 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DryBulbTemperatureMeasurement".
map:s_10 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#ExtraterrestrialDirectNormalRadiation".
map:s_11 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ExtraterrestrialDirectNormalRadiationMeasurement".
map:s_12 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#HorizontalInfraredRadiationIntensity".
map:s_13 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/HorizontalInfraredRadiationIntensityMeasurement".
map:s_14 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#GlobalHorizontalRadiation".
map:s_15 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/GlobalHorizontalRadiationMeasurement".
map:s_16 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DirectNormalRadiation".
map:s_17 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DirectNormalRadiationMeasurement".
map:s_18 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DiffuseHorizontalRadiation".
map:s_19 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DiffuseHorizontalRadiationMeasurement".
map:s_2 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DewPointTemperature".
map:s_20 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#GlobalHorizontalIlluminance".
map:s_21 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/GlobalHorizontalIlluminanceMeasurement".
map:s_22 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DirectNormalIlluminance".
map:s_23 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DirectNormalIlluminanceMeasurement".
map:s_24 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DiffuseHorizontalIlluminance".
map:s_25 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DiffuseHorizontalIlluminanceMeasurement".
map:s_26 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#ZenithLuminance".
map:s_27 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ZenithLuminanceMeasurement".
map:s_28 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#WindDirection".
map:s_29 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/WindDirectionMeasurement".
map:s_3 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DewPointTemperatureMeasurement".
map:s_30 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#WindSpeed".
map:s_31 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/WindSpeedMeasurement".
map:s_32 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#TotalSkyCover".
map:s_33 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/TotalSkyCoverMeasurement".
map:s_34 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#OpaqueSkyCover".
map:s_35 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/OpaqueSkyCoverMeasurement".
map:s_36 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#Visibility".
map:s_37 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/VisibilityMeasurement".
map:s_38 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#CeilingHeight".
map:s_39 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/CeilingHeightMeasurement".
map:s_4 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#RelativeHumidity".
map:s_40 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#PrecipitableWater".
map:s_41 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/PrecipitableWaterMeasurement".
map:s_42 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#AerosolOpticalDepth".
map:s_43 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AerosolOpticalDepthMeasurement".
map:s_44 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#SnowDepth".
map:s_45 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/SnowDepthMeasurement".
map:s_46 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#DaysSinceLastSnowfall".
map:s_47 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/DaysSinceLastSnowfallMeasurement".
map:s_48 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#LiquidPrecipitationDepth".
map:s_49 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/LiquidPrecipitationDepthMeasurement".
map:s_5 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/RelativeHumidityMeasurement".
map:s_50 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#LiquidPrecipitationQuantity".
map:s_51 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/LiquidPrecipitationQuantityMeasurement".
map:s_52 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#{epwName}".
map:s_53 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#GroundTemperatureDepth/{groundTemperatureDepth}".
map:s_54 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#GroundConductivity/{groundTemperatureDepth}".
map:s_55 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#GroundDensity/{groundTemperatureDepth}".
map:s_56 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#GroundSpecificHeat/{groundTemperatureDepth}".
map:s_57 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#GroundTemperature/{groundTemperatureDepth}".
map:s_58 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/Device".
map:s_59 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/spatialThing/Point".
map:s_6 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#AtmosphericStationPressure".
map:s_60 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/def/weather#{typeOfPeriod}".
map:s_61 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{wmo}/{typeOfPeriod}/{season}".
map:s_62 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{epwName}".
map:s_7 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/AtmosphericStationPressureMeasurement".
map:s_8 a rr:SubjectMap;
    rr:constant "https://bimerr.iot.linkeddata.es/def/weather#ExtraterrestrialHorizontalRadiation".
map:s_9 a rr:SubjectMap;
    rr:template "https://bimerr.iot.linkeddata.es/resource/weather/{adm03}/{city}/{Year}-{Month}-{Day}-{Hour}/ExtraterrestrialHorizontalRadiationMeasurement".
map:source_0 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_1 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_10 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_11 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_12 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_13 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_14 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_15 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_16 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_17 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_18 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_19 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_2 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_20 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_21 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_22 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_23 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_24 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_25 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_26 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_27 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_28 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_29 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_3 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_30 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_31 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_32 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_33 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_34 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_35 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_36 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_37 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_38 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_39 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_4 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_40 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_41 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_42 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_43 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_44 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_45 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_46 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_47 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_48 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_49 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_5 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_50 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_51 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_52 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_53 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.groundTemperatures[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_54 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.groundTemperatures[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_55 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.groundTemperatures[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_56 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.groundTemperatures[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_57 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.groundTemperatures[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_58 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.location[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_59 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.location[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_6 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_60 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.typical_extremePeriods[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_61 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.typical_extremePeriods[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_62 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.typical_extremePeriods[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_7 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_8 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
map:source_9 a rml:LogicalSource;
    rml:source "../DataStorage/""" + epwName + """.json";
    rml:iterator "$.epw[*]";
    rml:referenceFormulation ql:JSONPath.
        """
    )

    document.close()