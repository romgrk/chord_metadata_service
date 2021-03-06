__all__ = [
    "VALID_DATA_USE_1",
    "VALID_PROJECT_1",
    "VALID_DATS_CREATORS",
    "INVALID_DATS_CREATORS",
    "valid_dataset_1",
    "dats_dataset",
    "TEST_SEARCH_QUERY_1",
    "TEST_SEARCH_QUERY_2",
    "TEST_FHIR_SEARCH_QUERY",
]


VALID_DATA_USE_1 = {
    "consent_code": {
        "primary_category": {"code": "GRU"},
        "secondary_categories": [
            {"code": "GSO"},
            {"code": "RU"}
        ]
    },
    "data_use_requirements": [
        {"code": "COL"},
        {"code": "MOR"},
        {"code": "US"}
    ]
}


VALID_PROJECT_1 = {
    "title": "Project 1",
    "description": "Some description",
}


VALID_DATS_CREATORS = [
      {
         "name": "1000 Genomes Project"
      }
    ]


INVALID_DATS_CREATORS = [
    {
        "fullName": "John, Doe",
        "lastName": "Doe",
        "firstName": "John",
        "affiliations": [
            {
                "name": "Medical Center"
            }
        ]
    },
    {
        "fullName": "Jane, Doe",
        "surname": "Doe",
        "firstName": "Jane",
        "affiliations": [
            {
                "organization": "Medical Center"
            }
        ]
    }
]


def valid_dataset_1(project_id):
    return {
        "title": "Dataset 1",
        "description": "Test Dataset",
        "data_use": VALID_DATA_USE_1,
        "project": project_id
    }


def dats_dataset(project_id, creators):
    return {
       "version": "1.0",
       "project": project_id,
       "privacy": "public open",
       "licenses": [
          {
             "name": "BY-NC-SA"
          }
       ],
       "creators": creators,
       "types": [
          {
             "information": {
                "value": "genomics"
             }
          }
       ],
       "title": "1000 Genomes Project",
       "description": "The 1000 Genomes Project provides a comprehensive description of common human variation by "
                      "applying a combination of whole-genome sequencing, deep exome sequencing and dense microarray "
                      "genotyping to a diverse set of 2504 individuals from 26 populations.  Over 88 million variants "
                      "are characterised, including >99% of SNP variants with a frequency of >1% for a variety of "
                      "ancestries.",
       "storedIn": {
          "name": "European Bioinformatics Institute"
       },
       "primaryPublications": [
          {
             "identifier": {
                "identifier": "https://doi.org/10.1038/nature15393"
             },
             "title": "A global reference for human genetic variation",
             "dates": [
                {
                   "type": {
                      "value": "Primary reference publication date"
                   },
                   "date": "2015-10-01 00:00:00"
                }
             ],
             "authors": [
                {
                   "name": "1000 Genomes Project"
                }
             ]
          }
       ],
       "isAbout": [
          {
             "identifier": {
                "identifier": "9606",
                "identifierSource": "https://www.ncbi.nlm.nih.gov/taxonomy/9606"
             },
             "name": "Homo sapiens"
          }
       ],
       "dates": [
          {
             "type": {
                "value": "CONP DATS JSON fileset creation date"
             },
             "date": "2019-06-17 13:16:33"
          }
       ],
       "hasPart": [],
       "extraProperties": [
          {
             "category": "contact",
             "values": [
                {
                   "value": "Jennifer Tremblay-Mercier, Research Co-ordinator, "
                            "jennifer.tremblay-mercier@douglas.mcgill.ca, 514-761-6131 #3329"
                }
             ]
          }
       ],
       "data_use": VALID_DATA_USE_1
    }


TEST_SEARCH_QUERY_1 = ["#eq", ["#resolve", "subject", "sex"], "FEMALE"]
TEST_SEARCH_QUERY_2 = ["#eq", ["#resolve", "subject", "sex"], "MALE"]
TEST_FHIR_SEARCH_QUERY = {"query": {"match": {"gender": "FEMALE"}}}
