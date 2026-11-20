# TTL Tuning Notes

- Use monotonic clocks to avoid wall-clock jump bugs.
- Keep `max_items` bounded to prevent unbounded memory growth.
