# Sampler Crawler using RQ

1. Ensure that Redis and MongoDB is running.

   ```
   $ redis-server
   ```

   ```
   $ mongod
   ```

2. Start worker process.

   ```
   (scraping) $ rq worker --exception-handler 'exception_handler.requeue_job'
   ```

3. Run crawler.

   ```
   (scraping) $ python crawl.py
   ```
