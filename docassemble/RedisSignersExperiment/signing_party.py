from docassemble.base.util import log, DARedis#, Individual, #, DAObject

redis = DARedis()
  
def amend_signer( url_args, key, value ):
  if 'action_key' in url_args:
    party_id = url_args['party_id']
    action_data = redis.get_data( url_args['action_key'] )

    # set party key
    action_data['parties'][ party_id ][ key ] = value
    redis.set_data( url_args[ 'action_key' ], action_data )
    return action_data['parties'][ party_id ]
  else:
    return None
  
def get_signer( url_args ):
  if 'action_key' in url_args:
    party_id = url_args['party_id']
    if party_id in redis.get_data( url_args['action_key'] )['parties']:
      return redis.get_data( url_args['action_key'] )['parties'][ party_id ]
    else:
      return False
  else:
    return False
