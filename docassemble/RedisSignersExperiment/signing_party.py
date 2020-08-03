from docassemble.base.util import DARedis, DAObject

# Use and save data in redis if possible
#class SigningParty(DAObject):
class SigningParty():
  # Only uses redis if url arguments exist to allow this module to be used independently of url arguments. Somewhere else will take care of authentication?
  #def init(self, url_args):
  def __init__(self, url_args):
    #super().init(*pargs, **kwargs)
    self.exists = False
    
    # In url_args there should be:
    # action_key, user_id, party_id

    if 'action_key' in url_args:
      self.exists = True
      self.redis = DARedis()
      redis = self.redis

      # These intermediate vars are actually useful
      self.action_key = url_args[ 'action_key' ]
      self.id = url_args['party_id']
      self.action_data = redis.get_data( self.action_key )
      parties = self.action_data['parties']
      self.user = parties[ url_args['user_id'] ]  # For sms message
      party = parties[ self.id ]
      #self.preview = self.action_data['preview']
      #self.preview = self.action_data['sign_doc']

      # Start as undefined when user first arrives?
      self.signature = valueOrNone( party, 'signature' )
      self.signature_date = valueOrNone( party, 'signature_date' )
      self.willing_to_sign = valueOrNone( party, 'willing_to_sign' )

  def amend(self, key, value):
    if self.exists:
      setattr( self.action_data['parties'][ self.id ], key, value ) #.setAttribute( key, value )
      self.redis.set_data( self.action_key, self.action_data )

def valueOrNone( dictionary, key ):
  try: return dictionary[ key ]
  except: return None