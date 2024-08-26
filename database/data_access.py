from utils import constants


class Queries:
    @staticmethod
    def get_properties():
        return f"""
            SELECT p.address, p.city, s.name as status, p.price, p.description
            FROM {constants.DB_NAME}.property as p
            JOIN(
                SELECT sh.property_id, sh.update_date, status.name
                FROM {constants.DB_NAME}.status_history sh
                JOIN {constants.DB_NAME}.status
                ON status.id = sh.status_id
                WHERE (property_id, update_date) IN (
                    SELECT property_id, MAX(update_date)
                    FROM {constants.DB_NAME}.status_history
                    GROUP BY property_id
                )
            ) as s
            ON s.property_id = p.id 
            WHERE s.name IN ('{constants.PRE_SALE_STATUS}', '{constants.SALE_STATUS}', '{constants.SOLD_STATUS}')
            AND (p.address != '' AND p.address IS NOT NULL)
            AND (p.city != '' AND p.city IS NOT NULL)
            AND (p.price > 0 AND p.city IS NOT NULL)
            AND (%s IS NULL OR p.year = %s)
            AND (%s IS NULL OR p.city = %s)
            AND (%s IS NULL OR s.name = %s)
            ORDER BY p.id;
        """
