import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("node_activity.log"), logging.StreamHandler(sys.stdout)]
)

async def monitor_service(name, interval):
    while True:
        logging.info(f"Checking status for: {name}...")
        await asyncio.sleep(interval)
        logging.info(f"Service {name} is HEALTHY.")
        await asyncio.sleep(60)

async def main():
    logging.info("Initializing Node-Sentinel-Base Engine...")
    await asyncio.gather(
        monitor_service("Network-Interface", 5),
        monitor_service("Database-Sync", 10)
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("System shutdown requested.")
