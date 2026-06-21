from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):

    def __init__(self):
        # Connection Variables
        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection to MongoClient
        self.client = MongoClient(f'mongodb://{HOST}:{PORT}/')
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]

    # Create method which returns a boolean depending on insertion success
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to add, because data parameter is empty")
            return False

    # Read method that returns the results of a query or an empty list
    #     results are returned in a Cursor and must be converted to an acceptable datatype
    def read(self, query):
        if query is not None:
            results = self.collection.find(query)
            return results
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            return []

    def read_rescue_operations_analytics(self):
        pipeline = [
            {
                # Focus strictly on urgent outcome statuses (e.g., Transfer/Rescue requests)
                '$match': {
                    'outcome_type': 'Transfer'
                }
            },
            {
                # Grouping by species to evaluate urgent incoming/outgoing volume
                '$group': {
                    '_id': '$animal_type',
                    'rescue_count': {'$sum': 1},
                    'raw_avg_age': {'$avg': '$age_upon_outcome_in_weeks'},
                    'raw_min_age': {'$min': '$age_upon_outcome_in_weeks'}
                }
            },
            {
                # Transforming the values into clean numbers
                '$project': {
                    '_id': 1,
                    'rescue_count': 1,
                    'average_rescue_age_weeks': {'$round': ['$raw_avg_age', 2]},
                    'youngest_rescue_age_weeks': {'$round': ['$raw_min_age', 2]}
                }
            },
            {
                # Sorting by the highest volume of urgent cases
                '$sort': {
                    'rescue_count': -1
                }
            }
        ]

        try:
            results = self.collection.aggregate(pipeline)
            return results
        except Exception as e:
            print(f"Rescue Operations Aggregation Failed: {e}")
            return []

    def read_type_analytics(self):
        pipeline = [
            {
                # Gather and compute raw numerical data buckets
                '$group': {
                    '_id': '$animal_type',
                    'total_count': {
                        '$sum': 1
                    },
                    'raw_avg': {
                        '$avg': '$age_upon_outcome_in_weeks'
                    },
                    'raw_min': {
                        '$min': '$age_upon_outcome_in_weeks'
                    },
                    'raw_max': {
                        '$max': '$age_upon_outcome_in_weeks'
                    }
                }
            },
            {
                # Transforming the values into clean numbers
                '$project': {
                    '_id': 1,
                    'total_count': 1,
                    'average_age_weeks': {
                        '$round': ['$raw_avg', 2]
                    },
                    'youngest_age_weeks': {
                        '$round': ['$raw_min', 2]
                    },
                    'oldest_age_weeks': {
                        '$round': ['$raw_max', 2]
                    }
                }
            },
            {
                # Sorting the final results by population volume
                '$sort': {
                    'total_count': -1
                }
            }
        ]

        try:
            results = self.collection.aggregate(pipeline)
            return results
        except Exception as e:
            print(f"Animal Type Aggregation Failed: {e}")
            return []

    def read_dog_volume(self):
        pipeline = [
            {
                # Only uses Dog documents from here on out
                '$match': {
                    'animal_type': 'Dog'
                }
            },
            {
                # Grouping by breed and extracting raw numerical calculations
                '$group': {
                    '_id': '$breed',
                    'breed_count': {
                        '$sum': 1
                    },
                    'raw_avg_age': {
                        '$avg': '$age_upon_outcome_in_weeks'
                    }
                }
            },
            {
                # Transforming the values into clean numbers
                '$project': {
                    '_id': 1,
                    'breed_count': 1,
                    'avg_age_weeks': {
                        '$round': ['$raw_avg_age', 2]
                    }
                }
            },
            {
                # Eliminating breeds with low numbers
                '$match': {
                    'breed_count': {
                        '$gte': 2
                    }
                }
            },
            {
                # Sorting the final results by descending
                '$sort': {
                    'breed_count': -1
                }
            }
        ]

        try:
            results = self.collection.aggregate(pipeline)
            return results
        except Exception as e:
            print(f"Dog Volume Aggregation Failed: {e}")
            return []

    # Update method that takes a query and new info, and updates all the document match to the query
    #     The method returns the number of documents updated, which must be displayed with the modified_count() method
    def update(self, query, info):
        num_updated = self.collection.update_many(query, {"$set": info})
        return num_updated

    # Delete method that deletes all documents matched to the query
    #     The method returns number of documents deleted, which must be displayed with the deleted_count() method
    def delete(self, query):
        num_deleted = self.collection.delete_many(query)
        return num_deleted


acc = AnimalShelter()
stats = acc.read_rescue_operations_analytics()
for stat in stats:
    print(stat)
