from docassemble.base.util import log, DARedis, Individual#, DAObject

redis = DARedis()
  
def amend_signer( data, key, value ):
  if 'interview_data_id' in data:
    party_id = data['party_id']
    action_data = redis.get_data( data['interview_data_id'] )

    # set party key
    action_data['parties'][ party_id ][ key ] = value
    redis.set_data( data[ 'interview_data_id' ], action_data )
    return action_data['parties'][ party_id ]
  else:
    return None
  
def get_signer( data ):
  if 'interview_data_id' in data:
    party_id = data['party_id']
    if party_id in redis.get_data( data['interview_data_id'] )['parties']:
      return redis.get_data( data['interview_data_id'] )['parties'][ party_id ]
    else:
      return False
  else:
    return False


# Unimplemented because I can't figure out how to make this
# remember that it's an `Individual` so that generic object
# stuff will work.
class Signer( Individual ):
  def init( self, *pargs, **kwargs ):
    super(Signer, self).init(*pargs, **kwargs)

    data = kwargs.get( 'data', {} )
    self.set_data( data )
    
    return self
  
  # So the data can be changed or set later? Not sure.
  def set_data(self, data):

    if data and 'interview_data_id' in data:
      self.id = data['party_id']
      if self.id in redis.get_data( data['interview_data_id'] )['parties']:
        self.exists = True
        party = redis.get_data( data['interview_data_id'] )['parties'][ self.id ]
        self.name.first = party['name']
        self.has_signed = party['has_signed']
        self.was_willing = party['willing_to_sign']
        return None

    self.exists = False
    return None