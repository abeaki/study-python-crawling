# Sampler Crawler using Celery

1. Ensure running RabbitMQ and MongoDB.

   ```
   $ rabbitmq-server
   ```

   ```
   $ mongod
   ```

2. Start worker process.

   ```
   (scraping) $ celery worker -A scraper_tasks
   ```

3. Run crawler.

   ```
   (scraping) $ python crawl.py
   ```
