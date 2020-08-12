from docassemble.base.util import log, DARedis#, Individual, #, DAObject

redis = DARedis()
  
def amend_signer( data, key, value ):
  if 'action_key' in data:
    party_id = data['party_id']
    action_data = redis.get_data( data['action_key'] )

    # set party key
    action_data['parties'][ party_id ][ key ] = value
    redis.set_data( data[ 'action_key' ], action_data )
    return action_data['parties'][ party_id ]
  else:
    return None
  
def get_signer( data ):
  
  #if 'action_key' in url_args:
  #  data = url_args
  #
  ## Will this error?
  #elif action_argument('action_key'):
  #  data = {
  #    #'parent_interview_data_id': action_argument('parent_interview_data_id'),
  #    'action_key': action_argument('action_key'),
  #    'party_id': action_argument('party_id')
  #  }

  if 'action_key' in data:
    party_id = data['party_id']
    if party_id in redis.get_data( data['action_key'] )['parties']:
      return redis.get_data( data['action_key'] )['parties'][ party_id ]
    else:
      return False
  else:
    return False
