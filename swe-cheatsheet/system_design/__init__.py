# Open ending questions allow you to show your strengths
# - focus your answer on what you know best

# Request latency
# - letter 1 byte
# - integer/datetimes 4 bytes
# - 1 bytes = 8 bits = 256 values
# - char 1 bytes, int & unsigned 4, long 8
# - 2^8=256, 2^32~=4 billion, 2^64~=17 billion gigabytes

"""
General approach

1. Ask a lot of clarifying question
- outline use cases, contraints, & assumptions
- goal, what to prioritize? speed, reliability, availability
- what is the load, size of input
- consistency

2. High level design
- inputs outputs
- components, db web server, queue, cache (updating), CDN, load balancer
- db replications, cron jobs
- offline

"""