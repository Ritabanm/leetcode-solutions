WITH invoice_totals AS (
  SELECT
    p.invoice_id,
    SUM(pr.price * p.quantity) AS total_price
  FROM
    Purchases p
    JOIN Products pr ON p.product_id = pr.product_id
  GROUP BY
    p.invoice_id
),
max_invoice AS (
  SELECT
    invoice_id
  FROM
    invoice_totals
  WHERE
    total_price = (
      SELECT MAX(total_price) FROM invoice_totals
    )
  ORDER BY
    invoice_id
  LIMIT 1
)
SELECT
  p.product_id,
  p.quantity,
  pr.price * p.quantity AS price
FROM
  Purchases p
  JOIN Products pr ON p.product_id = pr.product_id
  JOIN max_invoice mi ON p.invoice_id = mi.invoice_id;