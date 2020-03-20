from scholia.app import create_app
from scholia.config import config

app = create_app(
    text_to_topic_q_text_enabled=False,
    third_parties_enabled=True)
app.config['APPLICATION_ROOT'] = '/'

if __name__ == '__main__':
    app.run(debug=True, host=config.get('system', 'listen'),
            port=config.get('system', 'port'))
